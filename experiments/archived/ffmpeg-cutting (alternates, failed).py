# cutter.add_span('00:00:00', text['scene-times-deleted']['scene1'])
#
# for i in range(len(text['scene-times-deleted'])):
#     if i == len(text['scene-times-deleted']) - 1:
#         cutter.add_span(text['scene-times-deleted']['scene' + str(i + 1)], '0')
#     else:
#         if alternate_count <= len(text['scene-times-alternate']) / 2 and \
#                 text['scene-times-alternate']['scene' + str(alternate_count) + '-start'] < \
#                 text['scene-times-deleted']['scene' + str(i + 2)]:
#             cutter.add_span(text['scene-times-deleted']['scene' + str(i + 1)], \
#                             text['scene-times-alternate']['scene' + str(alternate_count) + '-start'])
#             cutter.add_span(text['scene-times-alternate']['scene' + str(alternate_count) + '-start'], \
#                             text['scene-times-alternate']['scene' + str(alternate_count) + '-end'])
#             alternate_count = alternate_count + 1
#
#             while alternate_count <= len(text['scene-times-alternate']) / 2 and \
#                     text['scene-times-alternate']['scene' + str(alternate_count) + '-start'] < \
#                     text['scene-times-deleted']['scene' + str(i + 2)]:
#                 cutter.add_span(text['scene-times-alternate']['scene' + str(alternate_count - 1) + '-end'], \
#                                 text['scene-times-alternate']['scene' + str(alternate_count) + '-start'])
#                 cutter.add_span(text['scene-times-alternate']['scene' + str(alternate_count) + '-start'], \
#                                 text['scene-times-alternate']['scene' + str(alternate_count) + '-end'])
#                 alternate_count = alternate_count + 1
#
#             cutter.add_span(text['scene-times-alternate']['scene' + str(alternate_count - 1) + '-end'], \
#                             text['scene-times-deleted']['scene' + str(i + 2)])
#
#         else:
#             cutter.add_span(text['scene-times-deleted']['scene' + str(i + 1)],
#                             text['scene-times-deleted']['scene' + str(i + 2)])