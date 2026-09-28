from modules.boot_system import boot_system
from modules.gemini import talk_to_gemini

def main():
    boot_system()

    while True:
        boss_input=input("You: ")

        if boss_input == "quit":
            print("JARVIS: GOOD BYE SIR ")
            exit()

        else:
            final_response=talk_to_gemini(boss_input)
            print(f'JARVIS: {final_response}')

if __name__=="__main__":
    main()



