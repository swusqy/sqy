#coding:gbk
"""
����Ŀ�꣺���RPSLS��Ϸ
���ߣ�������
ʱ�䣺2020��4��15��
"""

import random#�����������һ��ʵ��



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):#�Զ��庯��,���û����������ת��Ϊ����
	"""
    ����Ϸ�����Ӧ����ͬ������
    """
	if name=="ʯͷ":
		a=0
	elif name=="ʷ����":
		a=1
	elif name=="��":
		a=2
	elif name=="����":
		a=3
	elif name=="����": 
		a=4
	else:	
		a="Error: No Correct Name"#�������Ĳ���Ҫ������
	return a				
def number_to_name(number):#�������Զ����ɵ�����Ϊ����
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    if number==0:
        b="ʯͷ"
    elif number==1:
        b="ʷ����"
    elif number==2:
        b="��"
    elif number==3:
        b="����"
    elif number==4: 
        b="����" 
    return b
def rpsls(choice_name):#����RPSLS���򣬱Ƚϵ������ɵ������û����������
    player_choice_number=name_to_number(choice_name)
    x=player_choice_number
    comp_number=random.randrange(0,4)#������������ɵ�ʵ����Χ������0-4
    y=comp_number
    print("�������ѡ���ǣ�")
    print(number_to_name(y))#���Զ��庯���������Զ����ɵ�����Ϊ�������
    if x==y:
        print("ƽ�ֿ�")
    elif x==0 and (y==3 or y==4):
	    print("��Ӯ��!")
    elif x==1 and (y==0 or y==4):
        print("��Ӯ��!")
    elif x==2 and (y==0 or y==1):
        print("��Ӯ��!")	 
    elif x==3 and (y==1 or y==2):
	    print("��Ӯ��!")					
    elif x==4 and (y==2 or y==3):
	    print("��Ӯ��!")
    elif x=="Error: No Correct Name":
	    print("Error: No Correct Name")
    else:
	    print("�����Ӯ��")    			
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


