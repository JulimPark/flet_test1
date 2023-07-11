import flet as ft
from flet import BorderSide
from flet import RoundedRectangleBorder
import pandas as pd
import ast
import sys
import os.path



def main(page: ft.Page):
    page.title = '수학클리닉+필요와충분 학생용 APP'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # answer_list = [1,3,2,4,5,6,10,4,22,-3]
    student_dict = {'박토순':'123','박핑코':'123','박흑코':'123','':''}
    # kunters = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11']
    kunters = [k+1 for k in range(500)]
    CWD = os.path.abspath(os.path.dirname(sys.executable))    #  추가 파일이 변형되어도 사용가능한 경로 작성
    print(CWD)
    df = pd.DataFrame(pd.read_csv(f'exam_data.csv'))
    test_num_list = df.시험고유번호.to_list()
    
    def close_dlg(e):
        dlg_modal.open = False
        page.update()
    
    def close_dlg2(e):
        dlg_modal2.open = False
        page.update()
    
    def close_dlg3(e):
        dlg_modal3.open = False
        page.update()
        
    def close_dlg5(e):
        dlg_modal5.open = False
        page.update()
        
    def init_page(e):
        page.clean()
        main_page()     
        dlg_modal2.open = False
        page.update()
    
    def load_exam(e):
        dlg_modal4.open = False
        page.clean()
        lv = ft.ListView(expand=True, spacing=10)
        for i in range(len(answer_list)):
            if str(answer_list[i]) in ['1','2','3','4','5']:
                aa = ft.Row([ft.Text(f'{i+1}번',size=25,bgcolor='green',color='white',weight=ft.FontWeight.BOLD,),
                            ft.Text('문항의 정답을 입력하세요.',size=20,color='black')])
                lv.controls.append(aa)
                kunters[i] = ft.RadioGroup(content=ft.Row([
                    ft.Radio(value='1',label='1',fill_color={ft.MaterialState.DEFAULT: ft.colors.BLACK,ft.MaterialState.SELECTED: ft.colors.RED,}),
                    ft.Radio(value='2',label='2',fill_color={ft.MaterialState.DEFAULT: ft.colors.BLACK,ft.MaterialState.SELECTED: ft.colors.RED,}),
                    ft.Radio(value='3',label='3',fill_color={ft.MaterialState.DEFAULT: ft.colors.BLACK,ft.MaterialState.SELECTED: ft.colors.RED,}),
                    ft.Radio(value='4',label='4',fill_color={ft.MaterialState.DEFAULT: ft.colors.BLACK,ft.MaterialState.SELECTED: ft.colors.RED,}),
                    ft.Radio(value='5',label='5',fill_color={ft.MaterialState.DEFAULT: ft.colors.BLACK,ft.MaterialState.SELECTED: ft.colors.RED,})
                ]))
                
                lv.controls.append(kunters[i])
                bb =ft.Divider()
                lv.controls.append(bb)
            else:
                aa = ft.Row([ft.Text(f'{i+1}번',size=25,bgcolor='blue',color='white',weight=ft.FontWeight.BOLD),ft.Text('문항의 정답을 입력하세요.',size=20,color='black')])
                lv.controls.append(aa)
                kunters[i] = ft.TextField(label="정답입력",color='black',border='underlined')#, hint_text="힌트 텍스트")
                lv.controls.append(kunters[i])
                # bb =ft.Divider()
                # lv.controls.append(bb)
                pass
        dd = ft.Container(
        alignment=ft.alignment.center,bgcolor='#3E4857',
        content=ft.Row(controls=[ft.ElevatedButton(text='정답제출',icon=ft.icons.CLOUD_UPLOAD,icon_color='#A7C9FA',on_click=submit_button,scale=1.5,style=styles),
            ft.ElevatedButton(text='초 기 화',on_click=open_dlg_modal2,icon=ft.icons.REPLAY,scale=1.5,icon_color='#A7C9FA',style=styles),],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            spacing=3,),padding=ft.padding.all(30)
        )
        lv.controls.append(dd)
        page.add(lv)
    
    
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("응답 확인"),
        content=ft.Text("정답을 입력하지 않은 문항이 존재합니다."),
        actions=[ft.TextButton('Close',on_click=close_dlg)],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    
        
    dlg_modal2 = ft.AlertDialog(
        modal=True,
        title=ft.Text("제출 확인"),
        content=ft.Text("제출하지 않은 정답까지 초기화됩니다.\n계속하시겠습니까?"),
        actions=[ft.TextButton('YES',on_click=init_page),
                 ft.TextButton('No',on_click=close_dlg2)],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    
    
    dlg_modal3 = ft.AlertDialog(
        modal=True,
        title=ft.Text("아이디/암호 확인!"),
        content=ft.Text("아이디와 암호를 확인하세요"),
        actions=[ft.TextButton('Close',on_click=close_dlg3)],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    
    dlg_modal5 = ft.AlertDialog(
        modal=True,
        title=ft.Text("시험고유번호 확인!"),
        content=ft.Text("존재하지 않는 시험입니다.\n시험고유번호를 확인하세요"),
        actions=[ft.TextButton('Close',on_click=close_dlg5)],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    
    def open_dlg_modal(*arg):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        
    
    def open_dlg_modal2(*arg):
        page.dialog = dlg_modal2
        dlg_modal2.open = True
        page.update()
        
    def open_dlg_modal3(*arg):
        page.dialog = dlg_modal3
        dlg_modal3.open = True
        page.update()
        
        

    def open_dlg_modal5(*arg):
        page.dialog = dlg_modal5
        dlg_modal5.open = True
        page.update()
        
    def choice_modal(*arg):
        global test_name,dlg_modal4,answer_list,df2
        try:
            test_nums = int(test_num.value)
        except:
            test_nums = 9999999
        if test_nums in test_num_list:
            df2 = df[df['시험고유번호']==test_nums].loc[:,]
            test_name = df2.iat[0,1]
            answer_list = ast.literal_eval(df2.iat[0,5])
            
            def close_dlg4(e):
                dlg_modal4.open = False
                page.update()
                
            dlg_modal4 = ft.AlertDialog(
                modal=True,
                title=ft.Text("시험명 확인"),
                content=ft.Text(f"{test_name}\n시험을 시작하시겠습니까?"),
                actions=[ft.TextButton('YES',on_click=load_exam),
                        ft.TextButton('No',on_click=close_dlg4)],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
            
            def open_dlg_modal4(*arg):
                page.dialog = dlg_modal4
                dlg_modal4.open = True
                page.update()
                
            open_dlg_modal4()
        else:
            open_dlg_modal5()
            
        
    
    def submit_button(e):
        stu_ans_list = []
        
        for i in range(len(answer_list)):
            stu_ans_list.append(kunters[i].value)
        if (None in stu_ans_list) | ('' in stu_ans_list):
            open_dlg_modal()
        else:
            print(stu_ans_list)
    
    
    def reset_button(e):
        page.clean()
        login_page()
        
    def login_button(e):
        stu_list = student_dict.keys()
        stu_id = log_id.value
        stu_pass = log_pass.value
        
        if stu_id in stu_list:
            if student_dict[stu_id]==stu_pass :
                page.clean()
                main_page()
            else:
                open_dlg_modal3()
        else:
            open_dlg_modal3()
            page.clean()
            login_page()
    
    
    def choice_exam(e):
        global test_num
        page.clean()
        page.title = f"{log_id.value} 학생을 위한 시험 선택 화면"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = '#FFFFFF'
        test_num = ft.TextField(prefix_icon=ft.icons.PIN,label='시험고유번호',label_style=ft.TextStyle(color='blue'),color='black')
        choice_exam_cl = ft.Column(width=300,height=180,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text('시험고유번호를 입력하세요',color='black',size=20),
                                        test_num,
                                        ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                                            ft.ElevatedButton("뒤로 가기",scale=1.2,icon=ft.icons.FIRST_PAGE,icon_color="pink600",on_click=main_page,style=styles),
                                            ft.ElevatedButton("시험 시작",scale=1.2,icon=ft.icons.TIMER,icon_color="blue400",on_click=choice_modal,style=styles)])
                                        ])
        page.add(choice_exam_cl)
    
    
    def main_page(*arg):
        page.clean()
        page.title = f"{log_id.value} 학생을 위한 메인 화면"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = '#FFFFFF'
        page.add(
            ft.Column(alignment=ft.CrossAxisAlignment.CENTER,spacing=100,
                      controls=[
                    ft.ElevatedButton("정답 입력",
                        icon=ft.icons.EDIT_SQUARE,
                        icon_color="blue400",on_click=choice_exam,
                        scale=3,
                        
                    ),
                    ft.ElevatedButton("통계 보기",
                        icon=ft.icons.SHOW_CHART,
                        icon_color="pink600",scale=3
                        
                    ),
                ]
            ),
        )
        
    def login_page():
        global log_id,log_pass
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = 'white'
        log_id = ft.TextField(border_color='gray',color='blue',label='사용자 이름')
        log_pass = ft.TextField(border_color='gray',color='blue',label='사용자 암호',password=True)
        log_page = ft.Column(width=300,horizontal_alignment=ft.MainAxisAlignment.CENTER
            ,controls=[
            ft.Text('사용자 이름과 암호를 입력하십시오.',color='red'),
            log_id,log_pass,
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.ElevatedButton('로그인',on_click=login_button),
                ft.ElevatedButton('초기화',on_click=reset_button),
                
            ])
        ])
        page.add(log_page)
        
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.THUMB_UP),
        leading_width=40,
        title=ft.Text("수학클리닉+필요와충분",style=ft.TextStyle(size=20,weight=ft.FontWeight.NORMAL)),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.FIRST_PAGE,on_click=main_page,tooltip='메인화면'),
            ft.IconButton(ft.icons.ACCOUNT_CIRCLE),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False,
                    ),
                ]
            ),
        ]
    )       
    
    
    
    styles = ft.ButtonStyle(
        color={ft.MaterialState.HOVERED: '#C5C9FA',
            ft.MaterialState.FOCUSED: ft.colors.BLUE,
            ft.MaterialState.DEFAULT: '#A7C9FA',},
        bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": '#323436'},
        padding={ft.MaterialState.HOVERED: 15},
        overlay_color=ft.colors.TRANSPARENT,
        elevation={"pressed": 0, "": 1},
        animation_duration=500,
        side={ft.MaterialState.DEFAULT: BorderSide(1, '#3E4857'),
            ft.MaterialState.HOVERED: BorderSide(2, '#A7C9FA'),},
        shape={ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
            ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),}
    )
    login_page()
    
    
    
ft.app(target=main)


