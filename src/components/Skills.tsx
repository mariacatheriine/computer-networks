import React from 'react';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

const Skills = () => {
  const skillCategories = [
    {
      title: 'Programming Languages',
      skills: ['Python', 'Java', 'C', 'JavaScript'],
      icon: '💻'
    },
    {
      title: 'Web Technologies',
      skills: ['HTML', 'CSS', 'JavaScript'],
      icon: '🌐'
    },
    {
      title: 'Currently Learning',
      skills: ['React', 'Node.js', 'Database Systems', 'Algorithms'],
      icon: '📚'
    }
  ];

  return (
    <section id="skills" className="py-20 bg-background">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-6">
            Skills & Technologies
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Here are the programming languages and technologies I'm familiar with, 
            along with areas I'm currently exploring.
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          {skillCategories.map((category, index) => (
            <Card key={index} className="p-8 bg-card shadow-soft hover:shadow-elegant transition-all duration-300">
              <div className="text-center mb-6">
                <div className="text-4xl mb-4">{category.icon}</div>
                <h3 className="text-2xl font-semibold text-foreground">
                  {category.title}
                </h3>
              </div>
              
              <div className="flex flex-wrap gap-3 justify-center">
                {category.skills.map((skill, skillIndex) => (
                  <Badge 
                    key={skillIndex}
                    variant="secondary"
                    className="px-4 py-2 text-sm font-medium"
                  >
                    {skill}
                  </Badge>
                ))}
              </div>
            </Card>
          ))}
        </div>
        
        <div className="mt-16 text-center">
          <Card className="p-8 bg-gradient-primary text-primary-foreground max-w-4xl mx-auto">
            <h3 className="text-2xl font-semibold mb-4">
              Always Learning, Always Growing
            </h3>
            <p className="text-lg opacity-90">
              As a Computer Science student, I believe in continuous learning and staying 
              updated with the latest technologies. I'm always excited to take on new 
              challenges and expand my skill set.
            </p>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default Skills;