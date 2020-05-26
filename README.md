# Spam Detection

## About this project
This project was built to AI discipline at University Federal of Ouro Preto. Its main goal is apply a simple artificial neural network (Perceptron) to detect spam.

## Introduction
E-mail, one of the oldest and most widely used services on the Internet, is also the most widely used medium for the indiscriminate sending of unsolicited messages, known as spam. Due to the wide variety of techniques used to send spam, this type of email is a problem that is still far from being solved. This work aims to present one of the main spam detection techniques, which is the use of an ANN (Artificial Neural Network) for spam detection.

## Perceptron
Rosenblatt's Perceptron was developed to solve the pattern recognition problem. This is a type of task that human beings do without any apparent effort and almost instantly. However, it is one of the most difficult problems to be solved by a machine.

#### Neuron Structure
In its simplest form, the neuron model consists of, input signals, synaptic weights, a bias, an additive function, an activation function and an output.
<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/40616142/82514184-72121080-9aeb-11ea-9ae0-68b375c55b7b.jpg">
</p>

Perceptron is able to learn concepts, being able to answer with 1 `true` or 0 `false` for the entries that are granted to it, training repeatedly the examples that are presented to it.

#### Training Perceptron
For the Perceptron neuron to be able to learn concepts, it is necessary to train it repeatedly until it is able to classify in the best possible way. In this project, the data were separated into **60%** of samples for training and **40%** for testing, being random samples to avoid what we call “overfitting”, where it can only predict samples with a certain type of characteristic.  
At the end of this process, with the appropriate choice of training data set, the network is able to estimate output variables for unknown input data, this procedure is called prediction. These simple networks are capable of estimating only linearly separable problems. For more complex problems, a model with more internal layers was proposed, which proved to be capable of estimating non-linear input-output relations.

#### Steps of the training algorithm
The training algorithm is defined in basically 4 steps:
  1. Initialize the synaptic weights with random values.
  2. Applies the input signals to the additive function.
  3. Calculate current output, performed by the activation function, if the sum result is greater than or equal to 0, `returns 1`, otherwise, `returns 0`.
  4. Update weight, this update is done using the formula:  
  <p align="center">
    <img src="https://user-images.githubusercontent.com/40616142/82524619-cf1ac000-9b05-11ea-98f4-eecebfead824.png">
  </p>

  *Labels:*
  <p align="left">
    <img src="https://user-images.githubusercontent.com/40616142/82525105-0047c000-9b07-11ea-8a74-c1a1a5762182.jpg">
  </p>
<p align="left">
  
***All labels informations are in portuguese***. <span>&#x1f1e7;&#x1f1f7;</span>
</p>

After the algorithm runs through all the samples, the error between the predicted output and the actual output is calculated. In this project, the Cross Entropy method was used to verify the quality of the metric, the cross entropy algorithm interprets the training signal and the network outputs as probabilities and the algorithm minimizes the difference between them. We also have at the end of each sample, a term called epoch, where it is counted to determine the number of epochs that the algorithm went through to finish the training.

The method for training the algorithm is an error reducer, we must establish a stopping criterion, as we will hardly be able to arrive at a perfect algorithm, that is, with `error = 0`.

I developed two methods to finish the training, `stop by minimum error`, where the algorithm analyzes your samples until you find a minimum error passed by parameter for training function, or the `stop method by number of epoch`, where we define a maximum number of epoch that the algorithm can process, if it finds that number, its training is ended.

## Results
The validation of the project proposal took place through tests carried out with the ANN (Artificial Neural Network). We can consider the positive results if the neural network was able to generalize the relation extracted from the unknown data, confirming that its training was in the most appropriate way possible.

To perform a performance comparison of the trained algorithm, two analyzes were performed, changing the learning rate parameter, with rates of 10% and 25% respectively. The Tables inform the result of the data collected during the training of the algorithm, 8 trainings were carried out, increasing its amount of time to verify its accuracy.

#### Table 1: Learning Rate 10%
<p align="center">
  <img src="https://user-images.githubusercontent.com/40616142/82520240-0aaf8d00-9afa-11ea-9989-2bd0f4899b70.jpg">
</p>

#### Table 2: Learning Rate 25%
<p align="center">
  <img src="https://user-images.githubusercontent.com/40616142/82520430-890c2f00-9afa-11ea-8883-df1cc848ab63.jpg">
</p>

### Performance

For a learning rate of 10% we obtained the following performance:  

**Average Sensitivity:** 0.85  
**Average Specificity:** 0.79  
**Average Accuracy:** 81.12%  
**Average Error:** 7.93  
**Average Epoch:** 8875  
**Average Time:** 446.75 seg.  
  
Analyzing the performance with a learning rate of 25% we obtained the following result:  
  
**Average Sensitivity:** 0.63  
**Average Specificity:** 0.89  
**Average Accuracy:** 78.5%  
**Average Error:** 7.82  
**Average Epoch:** 8875  
**Average Time:** 459.62 seg.

### Performance Graph
The graph below indicate the relationship `Error x Number` of seasons, showing the performance of the algorithm over the seasons, linked to the confusion matrix of their respective samples.

***OBS**: Just one graphic was chosen to represent the other training sessions, which was the graphic related to training 6.*
<p align="center">
  <img src="https://user-images.githubusercontent.com/40616142/82522106-cc689c80-9afe-11ea-8d07-25f079df5407.jpg">
</p>

# Conclusion
Spam is a problem that is still far from being solved, despite the fact that e-mail is present in the lives of most people today. In addition to user annoyance, spam can cause problems such as the generation of additional computational costs and expenses with technology and infrastructure to detect this content.  

We realized that the spam detection algorithm with a 10% learning rate achieved a better result than the 25%, due to the fact that the true gradient descent requires infinitesimal steps to be taken. Thus, the greater this constant, increasing the learning rate, the greater the change in weights, which can lead to an oscillation of the model on the error surface. The ideal scenario would be to use the highest possible learning rate that would not lead to a high oscillation, which would result in faster and more efficient training.

