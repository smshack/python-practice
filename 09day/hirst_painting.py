###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram # 이미지의 색상을 추출하는 모듈

rgb_colors = []
colors = colorgram.extract('C:\\Users\\jerry\\Documents\\python\\audio_streaming_google\\pythonpractice\\09day\\image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

for idx,val in enumerate(rgb_colors):
    print(idx,val)