import os
os.environ["OMP_NUM_THREADS"] = "1"
import cv2
from .utils.image_transforms import to_tensor, unsqueeze

def run_model(self):
    if self.runtime == "ONNX" or self.runtime == "Default (ONNX)":
        frame = cv2.resize(self.current_image_gray, (256, 256))
        frame = to_tensor(frame)
        frame = unsqueeze(frame,0)
        out = self.sess.run([self.output_name], {self.input_name: frame})
        output = out[0][0]

        output = self.one_euro_filter(output)

        for i in range(len(output)):  # Clip values between 0 - 1
            output[i] = max(min(output[i], 1), 0)

        self.output = output
