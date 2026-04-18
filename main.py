from db import init_db
from post_service import create_post, get_all_posts, get_post, delete_post
from utils import banner, menu

def run():
    init_db()
    banner()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            create_post(title, content)
            print("✔ Post created!\n")

        elif choice == "2":
            posts = get_all_posts()
            print("\n--- POSTS ---")
            for p in posts:
                print(f"{p[0]} | {p[1]} | {p[2]}")
            print()

        elif choice == "3":
            pid = input("Post ID: ")
            post = get_post(pid)
            if post:
                print("\n--- POST DETAIL ---")
                print("ID:", post[0])
                print("Title:", post[1])
                print("Content:", post[2])
                print("Time:", post[3])
            else:
                print("Not found!")

        elif choice == "4":
            pid = input("Delete ID: ")
            delete_post(pid)
            print("Deleted!\n")

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run()
