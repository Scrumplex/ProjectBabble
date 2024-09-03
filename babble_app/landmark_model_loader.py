import os
os.environ["OMP_NUM_THREADS"] = "1"
import cv2
import .utils.image_transforms as transforms

def run_model(self): # Replace transforms n shit for the pfld model
    if self.runtime == "ONNX" or self.runtime == "Default (ONNX)":
        frame = cv2.resize(self.current_image_gray, (256, 256))
        frame = transforms.to_tensor(frame)
        frame = transforms.unsqueeze(frame,0)
        out = self.sess.run([self.output_name], {self.input_name: frame})
        output = out[0][0]

        output = self.one_euro_filter(output)

        for i in range(len(output)):  # Clip values between 0 - 1
            output[i] = max(min(output[i], 1), 0)

        self.output = output


def write_image(self): # Debug function for development, remove once pfld is implemented. 
    frame = cv2.resize(self.current_image_gray, (256, 256))
    cv2.imwrite("yeah.png", frame)
    print("Image Wrote")
    self.output = (0, 0, 100, 100)
