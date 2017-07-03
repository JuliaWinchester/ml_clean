from os import listdir
from os.path import isfile, join
from subprocess import call

ml_server_bin = '/Applications/meshlab.app/Contents/MacOS/meshlabserver'
ml_script = '/Users/julie/Code/ml_clean/ml_clean.mlx'
mesh_dir = '/Users/julie/data/prime/derived/simp10ksmooth100'
output_dir = '/Users/julie/data/prime/derived/simp10ksmooth100mlclean'

for file in [f for f in listdir(mesh_dir) if isfile(join(mesh_dir, f))]:
	out_file = join(output_dir, file[:-4] + '-mlc.ply')
	# Example call: meshlabserver - input.ply -o output.ply -s script.mlx
	call([ml_server_bin, '-i', join(mesh_dir, file), \
		 '-o', join(output_dir, out_file), '-s', ml_script])

