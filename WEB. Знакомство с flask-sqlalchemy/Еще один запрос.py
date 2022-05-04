def main():
    global_init(input())
    session = create_session()
    res = []
    hours = {}
    department = session.query(Department).filter(Department.id == 1).first()
    for lst in department.members.split(', '):
        arr = list(map(int, lst))
        for num in arr:
            for job in session.query(Jobs).all():
                if num in [int(x) for x in job.collaborators.split(', ')]:
                    hours[num] = hours.get(num, 0) + job.work_size
            if hours[num] > 25:
                res.append(num)
    for user in session.query(User).all():
        if user.id in res:
            print(user.surname, user.name)


if __name__ == '__main__':
    main()
