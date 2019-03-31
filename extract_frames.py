import os
from subprocess import check_call

def worker(video_f):
    video_name = video_f.split('.')[0]
    folder = os.path.join('A2D/pngs320H', video_name)
    if not os.path.exists(folder):
        os.mkdir(folder)
    frame_path = os.path.join('A2D/pngs320H', video_name, '%05d.png')
    result = check_call(['ffmpeg', '-i', os.path.join('A2D/clips320H', video_f), frame_path])
    print(result)

if __name__ == "__main__":
    mat_root = 'A2D/Annotations/mat/'
    with open('data_split/test.txt') as f:
        lines = f.readlines()
        lines = [os.path.join(mat_root, line.strip() + '.mat') for line in lines]
        for anno in lines:
            if os.path.exists(anno):
                os.remove(anno)

    if not os.path.exists('A2D/pngs320H'):
        os.mkdir('A2D/pngs320H')
    lst = os.listdir('A2D/clips320H')
    for vid in lst:
        worker(vid)
