from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from app.routes.aws_helpers import ALLOWED_EXTENSIONS

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Post")



#  image = form.data["image"]
#  image.filename = get_unique_filename(image.filename)
#  upload = upload_file_to_s3(image)
#  print(upload)
#  if "url" not in upload:
#   return {ERROR: "HERE IS ERROR"}
#
#   new_post = Post(
#       image = upload["url"]
#   )
#
#

# return (
#         <form
#             onSubmit={handleSubmit}
#             encType="multipart/form-data"
#         >
#             <input
#               type="file"
#               accept="image/*"
#               onChange={(e) => setImage(e.target.files[0])}
#             />
#             <button type="submit">Submit</button>
#             {(imageLoading)&& <p>Loading...</p>}
#         </form>
#     )

# const UploadPicture = () => {
#     const [image, setImage] = useState(null);
#     const [imageLoading, setImageLoading] = useState(false);


#     const handleSubmit = async (e) => {
#         e.preventDefault();
#         const formData = new FormData();
#         formData.append("image", image);
#         // aws uploads can be a bit slow—displaying
#         // some sort of loading message is a good idea
#         setImageLoading(true);
#         await dispatch(createPost(formData));
#         history.push("/images");
#     }
#     // ...
# }

# export const createImage = (post) => async (dispatch) => {
#     const response = await fetch(`/images/new`, {
#       method: "POST",
#     //   headers: {
#     //     'Accept': 'application/json',
#     //     "Content-Type": "application/json",
#     //   },
#       body: post
#     });

#     if (response.ok) {
#         const { resPost } = await response.json();
#         dispatch(addPost(resPost));
#     } else {
#         console.log("There was an error making your post!")
#     }
# };

# import React, {useState} from "react";
# import { useHistory } from "react-router-dom";


# const UploadPicture = () => {
#     const history = useHistory(); // so that you can redirect after the image upload is successful
#     const [image, setImage] = useState(null);
#     const [imageLoading, setImageLoading] = useState(false);


#     const handleSubmit = async (e) => {
#         e.preventDefault();
#         const formData = new FormData();
#         formData.append("image", image);

#         // aws uploads can be a bit slow—displaying
#         // some sort of loading message is a good idea
#         setImageLoading(true);
#         await dispatch(createPost(formData));
#         history.push("/images");
#     }

#     return (
#         <form
#             onSubmit={handleSubmit}
#             encType="multipart/form-data"
#         >
#             <input
#               type="file"
#               accept="image/*"
#               onChange={(e) => setImage(e.target.files[0])}
#             />
#             <button type="submit">Submit</button>
#             {(imageLoading)&& <p>Loading...</p>}
#         </form>
#     )
# }

# export default UploadPicture;

# export const createImage = (post) => async (dispatch) => {
#     const response = await fetch(`/images/new`, {
#       method: "POST",
#       body: post
#     });

#     if (response.ok) {
#         const { resPost } = await response.json();
#         dispatch(addPost(resPost));
#     } else {
#         console.log("There was an error making your post!")
#     }
# };
