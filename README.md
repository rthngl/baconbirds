# baconbirds

This project recreates pictures of birds in the style of Francis Bacon's paintings (1930s-1980s). 

A few paintings and baconbirds-created images (20 training epochs):

![Slide1](https://user-images.githubusercontent.com/56600718/120390635-ce089b00-c2e2-11eb-8ae9-fbd711163f2d.png)


The code here is a lightly-adapted version of the Tensorflow implementation of CycleGAN written by Harry Yang and Nathan Silberman. 

[Their Original Code](https://github.com/leehomyc/cyclegan-1) | [CycleGAN Project](https://junyanz.github.io/CycleGAN/) | [Zhu et al. 2017](https://arxiv.org/pdf/1703.10593.pdf)


## abstract impressionism and style transfer

CycleGAN has been commonly implemented for style transfer, including patterns (i.e. horses to zebras) and textures (i.e. landscapes as Van Goghs). However, it is limited with respect to geometric changes (dogs to cats or apples to oranges can look a little lopsided, similarly [this notable failure case](https://junyanz.github.io/CycleGAN/images/failure_putin.jpg) demonstrates the limits of semantic segmentation + style transfer)

While somewhat abstracted examples of style transfer can be found ([Boshi et al. 2017](https://arxiv.org/pdf/1701.04928.pdf), [this Northwestern project](https://sally9805.github.io/Neural-Artistic-Style-Transfer/)) they still tend to work better when an overall textural style is applied (Hokusai or Mondrian) rather than an object-distortion style (Picasso).

This application of CycleGAN builds on the idea of adapting abstract impressionism by transferring the style of [Francis Bacon](https://francis-bacon.com/paintings) onto birds [via NABirds](https://dl.allaboutbirds.org/nabirds). We use 133 Bacon paintings (1930s-1990s -- we omit the very cubist works from the late 20s). We're aiming to see if any of the distortive/horror elements of Bacon's style persist in the generated images. 

Sample training data:

![Slide1](https://user-images.githubusercontent.com/56600718/119879946-9e235700-bee0-11eb-9fa6-07cc58735ca9.png) ![Slide2](https://user-images.githubusercontent.com/56600718/119879997-a8ddec00-bee0-11eb-8723-84695d42153c.png)


## running the code

We are reproducing here, for reference, instructions from [Yang and Silberman's implementation](https://github.com/leehomyc/cyclegan-1/blob/master/README.md), and adding a few notes.

1. This works best in an anaconda virtual environment. To start one:
    * for the ucla hoffman2 cluster (gpu)
      
	```bash
	qrsh -l gpu,P4
	module load python/anaconda3
	. "/u/local/apps/anaconda3/etc/profile.d/conda.sh"
	. $CONDA_DIR/etc/profile.d/conda.sh
	```
      
    * on mac osx
      
	```bash
	conda create -n fortf python=3.5 anaconda
	conda activate fortf
	```

2. Set up your training/testing data. 
    * I downloaded the horse2zebra dataset (for testing) and then just left all the directory names the same (sorry to my brother, who ). My baconbirds data are included here in the horse2zebra folder, but if you're making your own you'll need jpgs or pngs. The architecture is:
        
	 ```bash
	 - CycleGAN_TensorFlow      
	   |-input folder (horse2zebra)
	     |-trainA
	     |-trainB
	     |-testA
	     |-testB
	 ```

3. Create the csvs for loading/processing data. 
    * Edit cyclegan_datasets.py with
    
        * number of training/testing images for your larger dataset
        * jpg or png as your file format
        * paths to where your training and testing index files will go, something like: /path/to/CycleGAN_TensorFlow/input/horse2zebra_train.csv
    * Run create_cyclegan_dataset.py for your training AND testing data
    
	```bash
	python -m CycleGAN_TensorFlow.create_cyclegan_dataset --image_path_a=/path/to/trainA --image_path_b=/path/to/trainB --dataset_name="horse2zebra_train" --do_shuffle=0
	python -m CycleGAN_TensorFlow.create_cyclegan_dataset --image_path_a=/path/to/testA --image_path_b=/path/to/testB --dataset_name="horse2zebra_test" --do_shuffle=0

	```

4. Train the model.
    * Create or edit the config file (/CycleGAN_Tensorflow/configs/exp_01.json is the official CycleGAN base setup)
    * Run the main module (change the config/output links if necessary)
    
	```bash
	python -m CycleGAN_TensorFlow.main \
	    --to_train=1 \
	    --log_dir=CycleGAN_TensorFlow/output/cyclegan/exp_01 \
	    --config_filename=CycleGAN_TensorFlow/configs/exp_01.json
	```

5. Keep training from a stoppage/checkpoint.
    * If you stop, you can pick back up where you left off -- helpful for checking/adding more epochs. 
	```bash
	python -m CycleGAN_TensorFlow.main \
	    --to_train=2 \
	    --log_dir=CycleGAN_TensorFlow/output/cyclegan/exp_01 \
	    --config_filename=CycleGAN_TensorFlow/configs/exp_01.json \
	    --checkpoint_dir=CycleGAN_TensorFlow/output/cyclegan/exp_01/#timestamp#
	```

6. Test the model.
    * Make sure you assembled your testing dataset and created the index csv (step 3).
    * Runs on test data, saves to CycleGAN_Tensorflow/output/cyclegan/exp_01/#timestamp#
	```bash
	python -m CycleGAN_TensorFlow.main \
	    --to_train=0 \
	    --log_dir=CycleGAN_TensorFlow/output/cyclegan/exp_01 \
	    --config_filename=CycleGAN_TensorFlow/configs/exp_01_test.json \
	    --checkpoint_dir=CycleGAN_TensorFlow/output/cyclegan/exp_01/#old_timestamp# 
	```
	
## notes
   * Right now in main.py, images are saved using matplotlib.pyplot.imsave. Could also use imageio.imsave, if preferred. If you're taking the code from Yang and Silberman, you'll need to change from scipy.misc.imsave, which is depreciated.
   * If I don't run this in a conda environment, the tensorflow is pretty buggy (v1/v2/depreciated stuff/etc). It is also a bit of a mess in colab. Fair warning. Also, as of this writing, tf can't be used in python3.8. Worked well in 3.5.
   * I don't own and didn't make any of this, it's just for fun. That said, let me know if you have thoughts or find bugs!

## intermediate progress
  * After 20 epochs
  
  ![Slide3](https://user-images.githubusercontent.com/56600718/120390977-40797b00-c2e3-11eb-97a6-b1429cd3e621.png)

  * After 15 epochs
  
  ![Slide2](https://user-images.githubusercontent.com/56600718/120391026-4ff8c400-c2e3-11eb-83a2-0d75fc9118d5.png)
  
  * After 10 epochs
  
  ![Slide1](https://user-images.githubusercontent.com/56600718/120391051-5a1ac280-c2e3-11eb-8ccc-2d66ae8fe651.png)

  * After 6 epochs
   
  ![epoch6](https://user-images.githubusercontent.com/56600718/119878488-0709cf80-bedf-11eb-8310-339545fcf223.png)
 



