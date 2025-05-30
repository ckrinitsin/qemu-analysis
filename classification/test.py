from os import listdir, path

directory : str = "./test_input"

def test(classifier):
    for name in listdir(directory):
        with open(path.join(directory, name), "r") as file:
            sequence_to_classify = file.read()

        candidate_labels = ['semantic', 'other', 'mistranslation', 'instruction']
        result = classifier(sequence_to_classify, candidate_labels, multi_label=True)

        print(name)
        for label, score in zip(result["labels"], result["scores"]):
            print(f"{label}: {score:.3f}")
        print("")
