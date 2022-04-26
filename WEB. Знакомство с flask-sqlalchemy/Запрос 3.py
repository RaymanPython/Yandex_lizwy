def main():
    global_init(input())
    for user in create_session().query(User).filter(User.age < 18):
        print(f'<Colonist> {user.id} {user.surname} {user.name} {user.age} years')


if __name__ == '__main__':
    main()
