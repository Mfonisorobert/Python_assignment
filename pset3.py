# Loop through the bio_info dictionary and print key and values
def print_bio_info(bio_info):
    for key, value in bio_info.items():
        if key == "skills":
            print("My Skills are:")
            for skill in value:
                print(f"- {skill}")
        else:
            print(f"My {key.capitalize()} is {value}")


