import random
from time import sleep
import playsound

dict = {'가위': '✌️', '바위': '✊', '보': '🖐️', '묵': '✊', '찌': '✌️', '빠': '🖐️'}

win = 0
lose = 0
if_draw_retry = 0
player_right_of_command = 0
cpu_right_of_command = 0

cpu = ''
player_muk_chi_pa = ''
right_of_command_selected = ''
retry = 'y'

playsound.playsound('./mukchipa.mp3')
print("난 대학시절 묵찌빠를 전공했단 사아실")
print("네 놈을 이겨 눈물콧물 쏙 다 빼주마")
print("난 묵찌빠로 유학까지 다녀왔단 사아실")
print("네 놈을 이겨 가문의 이름 높이리")
print("")

while (True):

    while ((retry == 'y') or (retry == 'Y')):

        player = input("가위, 바위, 보 중 하나를 선택하세요: ")

        if (player == '가위') or (player == '바위') or (player == '보'):
            pass
        else:
            print("유효한 입력이 아닙니다.")

        while ((player == '가위') or (player == '바위') or (player == '보')):

            random_num = random.randrange(1, 4)

            if random_num == 1:
                cpu = '가위'
            elif random_num == 2:
                cpu = '바위'
            elif random_num == 3:
                cpu = '보'

            player_selected = dict[player]
            cpu_selected = dict[cpu]
            print(f'\n사용자: {player_selected}, 컴퓨터: {cpu_selected}')

            if (player == '가위' and cpu == '바위') or (player == '바위' and cpu == '보') or (player == '보' and cpu == '가위'):
                cpu_right_of_command += 1
                print("컴퓨터의 공격권\n")
                right_of_command_selected = cpu
            elif (player == '바위' and cpu == '가위') or (player == '가위' and cpu == '보') or (player == '보' and cpu == '바위'):
                player_right_of_command += 1
                print("사용자의 공격권\n")
                right_of_command_selected = player
            elif player == cpu:
                print("비겼습니다.\n")
                if_draw_retry += 1

            player = ''
            retry = ''

            if right_of_command_selected == '가위':
                right_of_command_selected = '찌'
            elif right_of_command_selected == '바위':
                right_of_command_selected = '묵'
            elif right_of_command_selected == '보':
                right_of_command_selected = '빠'

            while ((cpu_right_of_command == 1) or (player_right_of_command == 1)):
                sleep(1)
                print(f"{right_of_command_selected}...")
                sleep(1)
                print(f"{right_of_command_selected}...")
                sleep(1)

                while ((player_muk_chi_pa != '묵') and (player_muk_chi_pa != '찌') and (player_muk_chi_pa != '빠')):
                    player_muk_chi_pa = input("묵, 찌, 빠 중 하나를 선택하세요: ")
                    if (player_muk_chi_pa == '묵') or (player_muk_chi_pa == '찌') or (player_muk_chi_pa == '빠'):
                        pass
                    else:
                        print("유효한 입력이 아닙니다.")

                random_num = random.randrange(1, 4)

                if random_num == 1:
                    cpu_muk_chi_pa = '묵'
                elif random_num == 2:
                    cpu_muk_chi_pa = '찌'
                elif random_num == 3:
                    cpu_muk_chi_pa = '빠'

                player_selected = dict[player_muk_chi_pa]
                cpu_selected = dict[cpu_muk_chi_pa]
                print(f'\n사용자: {player_selected}, 컴퓨터: {cpu_selected}')

                if (cpu_right_of_command == 1):
                    if (player_muk_chi_pa == '찌' and cpu_muk_chi_pa == '묵') or (player_muk_chi_pa == '묵' and cpu_muk_chi_pa == '빠') or (player_muk_chi_pa == '빠' and cpu_muk_chi_pa == '찌'):
                        print("컴퓨터의 공격권\n")
                        right_of_command_selected = cpu_muk_chi_pa
                    elif (player_muk_chi_pa == '묵' and cpu_muk_chi_pa == '찌') or (player_muk_chi_pa == '찌' and cpu_muk_chi_pa == '빠') or (player_muk_chi_pa == '빠' and cpu_muk_chi_pa == '묵'):
                        player_right_of_command = 1
                        cpu_right_of_command = 0
                        print("사용자의 공격권\n")
                        right_of_command_selected = player_muk_chi_pa
                    elif player_muk_chi_pa == cpu_muk_chi_pa:
                        lose += 1
                        player_right_of_command = 0
                        cpu_right_of_command = 0
                        print("컴퓨터 승")

                elif (player_right_of_command == 1):
                    if (player_muk_chi_pa == '찌' and cpu_muk_chi_pa == '묵') or (player_muk_chi_pa == '묵' and cpu_muk_chi_pa == '빠') or (player_muk_chi_pa == '빠' and cpu_muk_chi_pa == '찌'):
                        player_right_of_command = 0
                        cpu_right_of_command = 1
                        print("컴퓨터의 공격권\n")
                        right_of_command_selected = cpu_muk_chi_pa
                    elif (player_muk_chi_pa == '묵' and cpu_muk_chi_pa == '찌') or (player_muk_chi_pa == '찌' and cpu_muk_chi_pa == '빠') or (player_muk_chi_pa == '빠' and cpu_muk_chi_pa == '묵'):
                        print("사용자의 공격권\n")
                        right_of_command_selected = player_muk_chi_pa
                    elif player_muk_chi_pa == cpu_muk_chi_pa:
                        win += 1
                        player_right_of_command = 0
                        cpu_right_of_command = 0
                        print("사용자 승")

                player_muk_chi_pa = ''

    if (if_draw_retry == 1):
        retry = 'y'
        if_draw_retry = 0
    else:
        retry = input("다시 하시겠습니까? (y/n): ")
        print("")

    if (retry == 'y') or (retry == 'Y'):
        pass
    elif (retry == 'n') or (retry == 'N'):
        print("게임을 종료합니다.")
        print(f'승: {win}, 패: {lose}')
        break
    else:
        print("y/Y 또는 n/N을 입력해주세요.")
