import project

if __name__ == "__main__":
    # try:
        project.load_env()
        project.project.run(debug = True, port=5001)
    # except Exception as error:
    #     print(error)
