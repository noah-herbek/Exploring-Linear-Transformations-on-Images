EXPLORING LINEAR TRANSFORMATIONS ON IMAGES

Summary: 
    This project explores the effects of various linear transformations on 2D
    images. Transformations include scaling, rotation, shearing, and reflection. Students will
    use Python and libraries such as math, NumPy, and PIL to manipulate images and apply
    these transformations.
Preparations:
    (1) Data Acquisition: Select a meaningful 2D image relevant to you or your friends.
    This can be a personal image or one obtained online. Provide a brief explanation
    of the image’s relevance to the group members.
    (2) Image Preprocessing: Use the Python Imaging Library (PIL) to read the image
    and name it image0. Convert image0 to a NumPy array named image0 np. Print
    the shape of image0 np to verify its dimensions.
Reference:
    https://github.com/songqsh/ma2071_v01/blob/master/src/image_transform_pil.
    ipynb
Linear Transformations: 
    Perform the following linear transformations on the x-y plane, assuming the center of the plane is the origin:
    (1) Transformation T1: Construct a linear transformation that scales image0 to half its size, and name it image1. Find the standard matrix of T1 and print image1.
    (2) Transformation T2: Construct a linear transformation that reflects image1 through the line y = 2x. Name the resulting image image2. Find the standard matrix of T2 and print image2.
    (3) Transformation T3: Construct a linear transformation that reflects image2 through the line y = −1/2x. Name the resulting image image3. Find the standard matrix of T3 and print image3.
    (4) Transformation T: Find the standard matrix of the linear transformation T = T2 ◦ T1. Apply T to image1 and print the resulting image.
    (5) Transformation T−1: Find the standard matrix of the inverse transformation of T. Apply T−1 to image3 and print the resulting image.
    (6) Favorite Transformation: Construct your favorite linear transformation and apply it to image1. You may use a composition of shearing, rotation, or any other trans- formation you prefer. Name the 
        resulting image image4. Find the standard matrix of your transformation and print image4.
Exploration and Analysis: 
    Explore the effects of different linear transformations on the
    image and observe how they change the image’s properties. For example, how does scaling
    affect the size and resolution of the image? How does rotation change the orientation of the image? How does shearing affect the shape of the image? How does reflection change the symmetry of the 
    image?
