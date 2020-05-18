from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
# ----
from myfw.mytorch.fw_nn_manager import fw_nn_manager
from myfw.mytorch.model.MLP import MLP as MLP
# ----
from myfw.mychainer.model.MLP import MLP as chainerMLP
# from myfw.mychainer.model.MLPAndClassifier import chainerMLPAndClassifier

class mlp_nn_manager(fw_nn_manager):

    # Dataset
    def set_dataset(self):

        if self.dataset == 'mnist':
            data_transform = ToTensor()
            # root="."
            root="..\data"
            self.train_dataset = MNIST(download=True, train=True, root=root, transform=data_transform)
            self.valid_dataset = MNIST(download=False, train=False, root=root, transform=data_transform)
        else:
            raise ValueError

    # model
    def set_model(self):

        if self.model_framework_type == 'pytorch':

            self.model = MLP()

        elif self.model_framework_type == 'chainer':

            # self.model = chainerMLPAndClassifier()
            self.model = chainerMLP()
 
            self.input_size = (28 * 28,)

        else:
            raise ValueError

        super(mlp_nn_manager, self).set_model()