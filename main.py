from datasets import Dataset, Audio
train_dataset = Dataset.from_csv("train.csv").cast_column('audio', Audio())
val_dataset = Dataset.from_csv("dev.csv").cast_column('audio', Audio())


train_dataset.push_to_hub("iapp/test-asr", split="train", token="<access token>")
val_dataset.push_to_hub("iapp/test-asr", split="val", token="<access token>")




