def main():
    global_init(input())

    session = create_session()

    for user in session.query(User).filter(User.address == "module_1",
                                           User.age < 21):
        user.address = "module_3"
    session.commit()


if __name__ == '__main__':
    main()
