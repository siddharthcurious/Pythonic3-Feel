***Mutex and Semaphores*** - Mutex and semaphore are kernel resources that provide synchronization services.

A mutex provides mutual exclusion, either producer or consumer can have the key (mutex) and proceed with their work. As long as the buffer is filled by producer, the consumer needs to wait, and vice versa.