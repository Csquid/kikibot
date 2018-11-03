from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, datetime

buttons_list = ['오늘','내일', 'today']
d_today = datetime.date.today()

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons': buttons_list
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘':
        today = "오늘 급식"

        return JsonResponse({
            'message': {
                'text': today
            },
            'keyboard': {
                'type':'buttons',
                'buttons': buttons_list
            }

        })

    elif datacontent == '내일':
        tomorrow = "내일 급식"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type':'buttons',
                'buttons': buttons_list
            }

        })

    elif datacontent == 'today':
        d_day = d_today.strftime('%Y/%m/%d')

        return JsonResponse({
            'message': {
                'text': d_day
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': buttons_list
            }
        })

    # return JsonResponse({
    #     'message': {
    #         'text': today_date + '의' + datacontent + '중식 메뉴입니다. \n\n' + get_menu(datacontent)
    #     },
    #     'keyboard': {
    #         'type': 'buttons',
    #         'buttons': ['오늘','내일']
    #     }
    # })

# def get_menu(re_datacontent):
#         if re_datacontent == '오늘':
#             today = "오늘 급식"
#
#             return JsonResponse({
#                     'message': {
#                         'text': today
#                     },
#                     'keyboard': {
#                         'type':'buttons',
#                         'buttons':['오늘','내일']
#                     }
#
#                 })
#
#         elif re_datacontent == '내일':
#             tomorrow = "내일 급식"
#
#             return JsonResponse({
#                     'message': {
#                         'text': tomorrow
#                     },
#                     'keyboard': {
#                         'type':'buttons',
#                         'buttons':['오늘','내일']
#                     }
#
#                 })
