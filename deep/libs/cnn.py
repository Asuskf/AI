# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:40:42 2020

@author: david
"""

import torch 

class CNN(torch.nn.Module):
    def __init__(self, input_shape, output_shape, device = "cpu"):
        """
        :param input_shape: Dimensión de la imagen, que supondremos viene reescalada a Cx84x84
        :param output_shape: Dimensión de la salida
        :param device: El dispositivo (CPU o CUDA) donde la CNN debe almacenar los valores a cada iteración
        """
        #input_shape Cx84x84
        super(CNN, self).__init__()
        self.device = device
        
        self.layer1 = torch.nn.Sequential(
                torch.nn.Conv2d(input_shape[0], 64, kernel_size = 4, stride = 2, padding = 1),
                torch.nn.ReLU()
                )
        
        self.layer2 = torch.nn.Sequential(
                torch.nn.Conv2d(64, 32, kernel_size = 4, stride = 2, padding = 0),
                torch.nn.ReLU()
                )
        
        self.layer3 = torch.nn.Sequential(
                torch.nn.Conv2d(32, 32, kernel_size = 3, stride = 1, padding = 0),
                torch.nn.ReLU()
                )
        
        self.out = torch.nn.Linear(18*18*32, output_shape)
        
    def forward(self, x):
        x = torch.from_numpy(x).float().to(self.device)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = x.view(x.shape[0], -1)
        x = self.out(x)
        return x