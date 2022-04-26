def main():
    global_init(input())

    session = create_session()
    collaborations = {x.id: len(x.collaborators.split())
                      for x in session.query(Jobs).all()}

    max_size = max(collaborations.values())
    ids = [x for x in collaborations if collaborations[x] == max_size]

    temp = [x.team_leader for x in session.query(Jobs).all() if x.id in ids]

    teamleaders = session.query(User).filter(User.id.in_(temp)).all()

    for member in teamleaders:
        print(member.name, member.surname)


if __name__ == '__main__':
    main()
