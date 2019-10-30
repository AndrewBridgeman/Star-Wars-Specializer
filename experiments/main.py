from editing import Editing

video = Editing('instructions.yaml')
#video.cut('files/original.mp4', 'files/special2.mp4', 'cuts')
video.assemble('cuts', 'final.mp4')
