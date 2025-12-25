import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


PROBLEMS = [
    {
        "question": "우리 동아리가 이번 발표회에서 주로 사용한 프로그래밍 언어는?",
        "answer": "파이썬",
        "hints": ["문법이 간결하여 배우기 쉬운 언어입니다.", "로고에 두 마리의 뱀이 그려져 있습니다.", "ㅍㅇㅆ (초성 힌트)"]
    },
    {
        "question": "파이썬 로고에 그려진 동물의 정체는?",
        "answer": "뱀",
        "hints": ["그리스 신화에 나오는 거대한 파충류에서 따온 이름입니다.", "발이 없고 몸이 길며 혀가 갈라져 있습니다.", "ㅂ (초성 힌트)"]
    },
    {
        "question": "코딩 중 발생한 오류를 찾아내어 고치는 과정을 무엇이라고 할까요?",
        "answer": "디버깅",
        "hints": ["영어 단어로 '벌레(Bug)'를 잡는다는 뜻에서 유래했습니다.", "프로그래머의 일과 중 가장 많은 시간을 차지합니다.", "ㄷㅂㄱ (초성 힌트)"]
    }
]

def run_game():
    remaining_problems = list(PROBLEMS)
    
    while True:
        if not remaining_problems:
            print("\n준비된 모든 문제를 다 풀었습니다! 문제 은행을 다시 채웁니다.")
            time.sleep(1.5)
            remaining_problems = list(PROBLEMS)
            
        current_problem = random.choice(remaining_problems)
        remaining_problems.remove(current_problem)
        
        question = current_problem["question"]
        secret_answer = current_problem["answer"].strip() 
        hints = current_problem["hints"]
        unlocked_hints = 0
        
        while True:
            clear_screen()
            print("=" * 60)
            print("🎲 [RANDOM MISSION] 암호 해독 센터")
            print(f"남은 미션 개수: {len(remaining_problems) + 1}개")
            print("=" * 60)
            print(f"\n📢 문제: {question}")
            print("-" * 60)
            print(f"💡 [현재 해금된 힌트: {unlocked_hints}/{len(hints)}개]")
            if unlocked_hints == 0:
                print("   (힌트가 필요하면 'h'를 입력하세요.)")
            else:
                for i in range(unlocked_hints):
                    print(f"   ✅ 힌트 {i+1}: {hints[i]}")
            print("-" * 60)
            
            user_input = input("👉 정답 입력 (또는 힌트보기 'h'): ").strip()

            if user_input.lower() == 'h':
                if unlocked_hints < len(hints):
                    unlocked_hints += 1
                    print("\n🔍 새로운 데이터 분석 중...")
                    time.sleep(0.8)
                else:
                    print("\n⚠️ 더 이상 제공할 힌트가 없습니다!")
                    time.sleep(1)
            
            elif user_input == secret_answer:
                print("\n" + "✨" * 20)
                print("🎊 [ACCESS GRANTED] 정답입니다!")
                print("✨" * 20)
                print(f"\n🔓 정답 확인: {secret_answer}")
                time.sleep(1)
                break
                
            elif user_input == "":
                continue
            else:
                print("\n❌ [ERROR] 암호가 일치하지 않습니다!")
                time.sleep(1)

       
        print("\n" + "-" * 60)
        print("🎮 다음 단계로 진행하시겠습니까?")
        retry = input("👉 '네' 또는 '아니오'를 입력하세요: ").strip()
        
        if retry == '네':
            print("\n🔄 새로운 문제를 불러오는 중...")
            time.sleep(1)
            continue
        elif retry == '아니오':
            print("\n👋 프로그램을 종료합니다. 수고하셨습니다!")
            time.sleep(2)
            break
        else:
            
            print("\n⚠️ 잘못된 입력입니다. 종료 화면으로 이동합니다.")
            time.sleep(1)
            break

if __name__ == "__main__":
    run_game()
