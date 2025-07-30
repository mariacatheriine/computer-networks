import React from 'react';
import { Card } from '@/components/ui/card';
import { GraduationCap, Code, BookOpen } from 'lucide-react';

const About = () => {
  return (
    <section id="about" className="py-20 bg-gradient-soft">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-6">
            About Me
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            I'm a passionate Computer Science and Engineering student at Government Engineering College, Thrissur, 
            dedicated to developing my coding skills and exploring the endless possibilities of technology.
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          <Card className="p-8 bg-card shadow-soft hover:shadow-elegant transition-all duration-300">
            <div className="text-center">
              <div className="w-16 h-16 bg-accent rounded-full flex items-center justify-center mx-auto mb-6">
                <GraduationCap className="w-8 h-8 text-accent-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-foreground mb-4">
                Education
              </h3>
              <p className="text-muted-foreground">
                Currently pursuing Computer Science & Engineering at GEC Thrissur, 
                building a strong foundation in computer science principles.
              </p>
            </div>
          </Card>
          
          <Card className="p-8 bg-card shadow-soft hover:shadow-elegant transition-all duration-300">
            <div className="text-center">
              <div className="w-16 h-16 bg-accent rounded-full flex items-center justify-center mx-auto mb-6">
                <Code className="w-8 h-8 text-accent-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-foreground mb-4">
                Development
              </h3>
              <p className="text-muted-foreground">
                Continuously developing my coding skills across multiple programming 
                languages and modern development practices.
              </p>
            </div>
          </Card>
          
          <Card className="p-8 bg-card shadow-soft hover:shadow-elegant transition-all duration-300">
            <div className="text-center">
              <div className="w-16 h-16 bg-accent rounded-full flex items-center justify-center mx-auto mb-6">
                <BookOpen className="w-8 h-8 text-accent-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-foreground mb-4">
                Learning
              </h3>
              <p className="text-muted-foreground">
                Passionate about staying current with technology trends and 
                continuously expanding my knowledge in computer science.
              </p>
            </div>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default About;