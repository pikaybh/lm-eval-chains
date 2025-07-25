from dotenv import load_dotenv
from fire import Fire
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langserve import RemoteRunnable

from evaluators import PiRatingEvaluator


load_dotenv()


@RunnableLambda
def pi_rating_inputs(data: dict) -> object:
    return{
        "site_image": [],
        "process_major_category": data["공정"],
        "process_minor_category": data["세부공정"],
        "equipment": data["설비"],
        "material": "",
        "task_description": data["작업 정보"],
    }
pi_rating_endpoint = RemoteRunnable("http://snucem1.iptime.org:8000/v1/openai/gpt-4.1/pi-ratings")
pi_rating_chain = pi_rating_inputs | pi_rating_endpoint

evaluator = PiRatingEvaluator(
    dataset_name="pi_ratings",
    target_chain=pi_rating_chain,
    core_model=ChatOpenAI("gpt-4.1"),
    prefix="갱폼 설치작업_합본파일 experiment"
)


def main():
    results = evaluator()
    print(results)

    results_df = results.to_dataframe()
    results_df.to_csv("output/pi_ratings_results.csv", index=False)


if __name__ == "__main__":
    Fire(main)