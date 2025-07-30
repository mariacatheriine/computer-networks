import React from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Mail, MapPin, Github, Linkedin } from 'lucide-react';

const Contact = () => {
  return (
    <section id="contact" className="py-20 bg-gradient-soft">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-6">
            Let's Connect
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            I'm always interested in connecting with fellow developers, students, 
            and professionals in the tech industry. Feel free to reach out!
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <Card className="p-8 md:p-12 bg-card shadow-elegant">
            <div className="grid md:grid-cols-2 gap-12">
              <div>
                <h3 className="text-2xl font-semibold text-foreground mb-6">
                  Get in Touch
                </h3>
                <p className="text-muted-foreground mb-8 leading-relaxed">
                  Whether you want to discuss technology, share learning resources, 
                  or collaborate on projects, I'd love to hear from you.
                </p>
                
                <div className="space-y-4">
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 bg-accent rounded-full flex items-center justify-center">
                      <Mail className="w-6 h-6 text-accent-foreground" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Email</p>
                      <p className="text-foreground font-medium">catherine.maria@example.com</p>
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 bg-accent rounded-full flex items-center justify-center">
                      <MapPin className="w-6 h-6 text-accent-foreground" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Location</p>
                      <p className="text-foreground font-medium">Thrissur, Kerala, India</p>
                    </div>
                  </div>
                </div>
              </div>
              
              <div>
                <h3 className="text-2xl font-semibold text-foreground mb-6">
                  Follow Me
                </h3>
                
                <div className="space-y-4">
                  <Button 
                    variant="outline" 
                    className="w-full justify-start gap-4 h-14 text-left"
                  >
                    <Github className="w-6 h-6" />
                    <div>
                      <p className="font-medium">GitHub</p>
                      <p className="text-sm text-muted-foreground">View my projects</p>
                    </div>
                  </Button>
                  
                  <Button 
                    variant="outline" 
                    className="w-full justify-start gap-4 h-14 text-left"
                  >
                    <Linkedin className="w-6 h-6" />
                    <div>
                      <p className="font-medium">LinkedIn</p>
                      <p className="text-sm text-muted-foreground">Professional network</p>
                    </div>
                  </Button>
                </div>
                
                <div className="mt-8">
                  <Button className="w-full bg-gradient-primary text-primary-foreground hover:shadow-elegant">
                    Send Message
                  </Button>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default Contact;