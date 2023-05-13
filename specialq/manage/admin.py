import pandas as pd
from specialq.models import SpecialSubmit
from specialq.serializers import SpecialSubmitSerializer


# def init_data():
#     # 初始化数据
#     paper_list = Paper.objects.all()
#     if len(paper_list) == 0:
#         print('paper list: ', len(paper_list))
#         df = pd.read_csv('paper/manage_temp/paper_source.csv')
#         for index in df.index:
#             paper_dict = df.loc[index, :].to_dict()
#             # print(dict)
#             paper = Paper(**paper_dict)
#             paper.save()


# def download_data():
#     papers = Paper.objects.all()
#     print('paper list: ', len(papers))
#
#     serializer = PaperSerializer(papers, many=True)
#
#     try:
#         df = pd.DataFrame(serializer.data)
#         df.to_csv('paper/manage_temp/paper_source_new.csv', index=False)
#         print('download_data successful!')
#     except Exception as e:
#         print('{log} download_data error:', e)


def delete_data():
    try:
        specials = SpecialSubmit.objects.all()
        for special in specials:
            special.delete()
        print('delete_data successful!')
    except Exception as e:
        print('{log} delete_data error:', e)


# def refresh_data():
#     papers = Paper.objects.filter(Locked__exact=True,
#                                   Complete__exact=False)
#     # 解锁
#     try:
#         for paper in papers:
#             paper.Locked = False
#             paper.save()
#         print('解锁 {} 条数据. '.format(len(papers)))
#     except Exception as e:
#         print('{log} refresh_data error:', e)
