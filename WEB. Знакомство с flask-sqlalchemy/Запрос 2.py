def main():
    global_init(input())
    session = create_session()
    for user in session.query(User).filter((User.address == 'module_1'),
                                           (User.speciality.notlike('%engineer%')),
                                           (User.position.notlike('%engineer%'))):
        print(user.id)


if __name__ == '__main__':
    main()
