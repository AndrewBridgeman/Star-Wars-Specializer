from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("clip1.mp4")
clip2 = VideoFileClip("clip2.mp4")
combined_clip = concatenate_videoclips([clip2,clip1], method = 'compose')
combined_clip=combined_clip.without_audio().set_audio(combined_clip.audio)
combined_clip.resize(width = 10, height = 500)
combined_clip.preview(fps = 1, audio = False)