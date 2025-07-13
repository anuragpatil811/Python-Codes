import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
# Generate a large grayscale matrix (simulating an image)
def generate_large_grayscale_matrix(size=500):
    """
    Create a synthetic grayscale image with various shapes and gradients
    to demonstrate edge detection.
    """
    matrix = np.zeros((size, size))
    
    # Add some geometric shapes and gradients
    # Rectangle
    matrix[100:200, 100:300] = 100
    
    # Diagonal gradient
    for i in range(size):
        for j in range(size):
            matrix[i, j] += (i + j) / (2 * size) * 255
    
    # Circle
    center_x, center_y = size // 2, size // 2
    for i in range(size):
        for j in range(size):
            if ((i - center_x) ** 2 + (j - center_y) ** 2 < 10000 and 
                ((i - center_x) ** 2 + (j - center_y) ** 2 > 9000)):
                matrix[i, j] = 200
    
    return matrix

# Define edge detection filter matrices
def create_edge_detection_filters():
    """
    Create 4 different edge detection filter matrices
    """
    # Sobel X-direction filter
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    
    # Sobel Y-direction filter
    sobel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    
    # Prewitt X-direction filter
    prewitt_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])
    
    # Laplacian filter (captures all directions)
    laplacian = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ])
    
    return [sobel_x, sobel_y, prewitt_x, laplacian]

# Perform convolution
def convolve2d(image, kernel):
    """
    2D convolution of image with a given kernel
    """
    # Get image and kernel dimensions
    image_h, image_w = image.shape
    kernel_h, kernel_w = kernel.shape
    
    # Compute output dimensions
    output_h = image_h - kernel_h + 1
    output_w = image_w - kernel_w + 1
    
    # Initialize output matrix
    output = np.zeros((output_h, output_w))
    
    # Perform convolution
    for i in range(output_h):
        for j in range(output_w):
            output[i, j] = np.sum(
                image[i:i+kernel_h, j:j+kernel_w] * kernel
            )
    
    return output

# Main execution
def main():
    # Generate large grayscale matrix
    original_image = generate_large_grayscale_matrix()
    
    # Create edge detection filters
    filters = create_edge_detection_filters()
    filter_names = ['Sobel X', 'Sobel Y', 'Prewitt X', 'Laplacian']
    
    # Visualize results
    plt.figure(figsize=(15, 10))
    
    # Original image
    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')
    
    # Edge detection results
    for i, (filter_matrix, name) in enumerate(zip(filters, filter_names), start=2):
        # Apply convolution
        edge_image = convolve2d(original_image, filter_matrix)
        
        # Normalize the edge image
        scaler = MinMaxScaler()
        edge_image_scaled = scaler.fit_transform(edge_image)
        
        plt.subplot(2, 3, i)
        plt.title(f'{name} Edge Detection')
        plt.imshow(edge_image_scaled, cmap='gray')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
