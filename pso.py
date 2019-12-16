from __future__ import division
import random
import math
def func1(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total
class Particle:
    def __init__(self,x0):
        self.position_i=[]       
        self.velocity_i=[]      
        self.pos_best_i=[]     
        self.err_best_i=-1    
        self.err_i=-1     
        for i in range(0,num_dimensions):
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(x0[i]) 
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.position_i) 
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i 
    def update_velocity(self,pos_best_g):
        w=0.5      
        c1=1        
        c2=2    
        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()
            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social 
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i] 
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1] 
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]
                
class PSO():
    def __init__(self,costFunc,x0,bounds,num_particles,maxiter):
        global num_dimensions
        num_dimensions=len(x0)
        err_best_g=-1             
        pos_best_g=[]               
        swarm=[]
        for i in range(0,num_particles):
            swarm.append(Particle(x0)) 
        i=0
        while i < maxiter: 
            for j in range(0,num_particles):
                swarm[j].evaluate(costFunc) 
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g=list(swarm[j].position_i)
                    err_best_g=float(swarm[j].err_i) 
            for j in range(0,num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            i+=1 
        print ('FINAL:')
        print (pos_best_g)
        print (err_best_g)
if __name__ == "__PSO__":
    main()
initial=[5,5]  
bounds=[(-10,10),(-10,10)]
PSO(func1,initial,bounds,num_particles=15,maxiter=30)
