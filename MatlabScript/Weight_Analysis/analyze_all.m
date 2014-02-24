function analyze_all()
subplot(221); 
analyze_drive()
xlabel('value');ylabel('weight');
subplot(222);
analyze_bass()
xlabel('value');ylabel('weight');
subplot(223);
analyze_mid()
xlabel('value');ylabel('weight');
subplot(224); 
analyze_treble()
xlabel('value');ylabel('weight');
end

