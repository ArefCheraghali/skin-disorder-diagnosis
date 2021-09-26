# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
from fastai.vision import *

folder = 'health'
folder = 'chickenpox'
folder = 'psuriasis'


path = Path('/')
dest = path/folder
dest.mkdir(parents=True, exist_ok=True)
path.ls()
classes = ['health','chickenpox','psuriasis']

download_images(path/folder/file, dest, max_pics=200)


for c in classes:
    print(c)
    verify_images(path/c, delete=True, max_size=500)

path

"""## View data"""

doc(ImageDataBunch.from_folder)

#np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.12,
        ds_tfms=get_transforms(do_flip=True, flip_vert=False, max_rotate=10.0, max_zoom=1.1, max_lighting=0.2, max_warp=0.2, p_affine=0.75, p_lighting=0.75), size=224, num_workers=4).normalize(imagenet_stats)

# If you already cleaned your data, run this cell instead of the one before
# np.random.seed(42)
# data = ImageDataBunch.from_csv(path, folder=".", valid_pct=0.2, csv_labels='cleaned.csv',
#         ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)


data.classes

data.show_batch(rows=3, figsize=(7,8))

data.classes, data.c, len(data.train_ds), len(data.valid_ds)

"""## Train model"""

learn = cnn_learner(data, models.resnet34, metrics=error_rate)

learn.fit_one_cycle(10)

learn.save('stage-1')

learn.unfreeze()

learn.lr_find()

# If the plot is not showing try to give a start and end learning rate
# learn.lr_find(start_lr=1e-5, end_lr=1e-1)
learn.recorder.plot()

learn.fit_one_cycle(4, max_lr=slice(1e-5,1e-3))

learn.save('stage-2')

"""## Interpretation"""

learn.load('stage-2');

interp = ClassificationInterpretation.from_learner(learn)

interp.plot_confusion_matrix()
 


learn.export()





learn.fit_one_cycle(40, slice(1e-6,1e-4))
