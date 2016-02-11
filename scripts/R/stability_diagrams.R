library(TDA)

n <- 100
x <- matrix(seq(0, 10, length.out=n), nrow=1, ncol=n)

y1 <- sin(x) + sin(.5*x+2) + 1.5*sin(2*x+2) + 5
y2 <- y1 + .25*rnorm(n)

plot(x, y1, 'l', col="red")
lines(x, y2, 'l', col="blue")

g1 <- gridDiag(X = x, FUNvalues = y1)
g2 <- gridDiag(X = x, FUNvalues = y2)

b1 <- g1$diagram[,2]
d1 <- g1$diagram[,3]

b2 <- g2$diagram[,2]
d2 <- g2$diagram[,3]

xmax <- 8
ymax <- 8

plot(b1, d1, pch=19, xlim=c(0, xmax), ylim=c(0, ymax), xlab="Birth", ylab="Death")
points(b2, d2, pch=16, col="green")
lines(c(0,10),c(0,10))
pdf("stability_diagram.pdf")
dev.off()


