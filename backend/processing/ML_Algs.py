import os
from Dataset_Loader import Dataset_Loader
from sklearn.metrics.pairwise import linear_kernel


def lin_kern(base, comp):
    sims = linear_kernel(base.drop("id", axis=1), comp.drop("id", axis=1))
    return sims


if __name__ == "__main__":
    loader = Dataset_Loader()
    print(loader.by_position["QB"][0].to_frame().transpose())
    print(lin_kern(loader.load_dataset("QB"),
                   loader.by_position["QB"][0].to_frame()))
