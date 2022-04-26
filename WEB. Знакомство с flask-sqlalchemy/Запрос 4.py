def main():
    global_init(input())
    session = create_session()
    for user in session.query(User).filter((User.position.like('%chief%')) |
                                           (User.position.like('%middle%'))):
        print(f'<Colonist> {user.id} {user.surname} {user.name} {user.position}')


if __name__ == '__main__':
    main()
