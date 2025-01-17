import torch
from torch.autograd import Variable

N, D_in, H, D_out = 64, 1000, 100, 10

x = Variable(torch.randn(N,D_in))
y = Variable(torch.randn(N,D_out),requires_grad=False)

model = torch.nn.Sequential(
	torch.nn.Linear(D_in,H),
	torch.nn.ReLU(),
	torch.nn.Linear(H,D_out),
)

loss_fn = torch.nn.MSELoss(size_average=False)

learning_rate = 1e-6

for t in range(50000):
	
	y_pred = model(x)
	loss = loss_fn(y_pred,y)
	print(t,loss.data[0])
	model.zero_grad()
	loss.backward()
	for param in model.parameters():
		param.data -= learning_rate * param.grad.data
    # print(t,loss.data[0])
    # model.zero_grad()
    # loss.backward()
    # for param in model.parameters():
    # 	param.data -= learning_rate * param.grad.data
