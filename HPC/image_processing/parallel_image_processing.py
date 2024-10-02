from mpi4py import MPI
import cv2
import numpy as np

def process_image(image_chunk):
    # Apply a filter (e.g., edge detection)
    return cv2.Sobel(image_chunk, cv2.CV_64F, 1, 0, ksize=5)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load and split image based on rank
if rank == 0:
    image = cv2.imread('test_image.jpg', 0)  # Load image as grayscale
    chunks = np.array_split(image, size, axis=0)
else:
    chunks = None

# Scatter image chunks
chunk = comm.scatter(chunks, root=0)

# Process each chunk
processed_chunk = process_image(chunk)

# Gather the processed chunks back
processed_image = comm.gather(processed_chunk, root=0)

if rank == 0:
    final_image = np.vstack(processed_image)
    cv2.imwrite('processed_image.jpg', final_image)
