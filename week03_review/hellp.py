name='harry'
print(name)

num=12
print(num)

number_status= 'ture'
print(number_status)


wizard={'name':'harry potter','age':40}
print(wizard)

wizard=[{'name': 'heechul', 'age':35}, {'name':'sunjung', 'age':49}]
print(wizard)


def is_adult(age):
    if age >= 20:
        print('성인입니다')  # 조건이 참이면 성인입니다를 출력
    else:
        print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력

print(is_adult(19))

# 조건을 여러 개 사용하고 싶을 때
def check_generation(age):
    if age > 120:
        print('와 19세기에 태어나셨군요!')
    elif age >= 80:
        print('80세 이상! 인생은 여든부터!')
    else:
        print('젊으시군요! 장래희망이 뭔가요?')


my_age = 55
check_generation(my_age)

print(check_generation(150))

wizards = [
    {'name': '해리', 'age': 40},
    {'name': '허마이오니', 'age': 40},
    {'name': '론', 'age': 41},
]

# 모든 마법사의 이름과 나이를 출력
for wizard in wizards:
    print(wizard['해리'], wizard['론'])