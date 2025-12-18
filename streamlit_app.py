import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("sk-proj-lwJcDXg")
SYSTEM_PROMPT = """
너는 청소년을 위한 심리적 지원 챗봇이다.

규칙:
- 절대 진단하거나 치료하지 않는다
- 공감과 감정 정리에 집중한다
- 위험하거나 극단적인 선택을 묘사하거나 설명하지 않는다
- 사용자가 매우 힘들어 보일 경우,
  신뢰할 수 있는 어른(부모, 교사, 상담사)이나
  전문 상담 도움을 받도록 부드럽게 권한다
- 판단하지 말고, 따뜻하고 차분한 말투를 사용한다
"""

def chat():
    print("🧠 심리상담 챗봇입니다. (종료: '종료')")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        user_input = input("너: ")

        if user_input == "종료":
            print("챗봇: 이야기해줘서 고마워. 언제든 다시 와도 돼 🙂")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        print("챗봇:", reply)

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat()
