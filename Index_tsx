import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Heart, Activity, Brain, Moon, TrendingUp, TriangleAlert as AlertTriangle, Phone, Calendar } from 'lucide-react-native';
import { router } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface HealthData {
  heartRate: number | null;
  bloodPressure: { systolic: number; diastolic: number } | null;
  mentalScore: number | null;
  sleepHours: number | null;
  lastUpdated: string;
}

export default function HomeScreen() {
  const [healthData, setHealthData] = useState<HealthData>({
    heartRate: null,
    bloodPressure: null,
    mentalScore: null,
    sleepHours: null,
    lastUpdated: new Date().toLocaleDateString(),
  });
  const [greeting, setGreeting] = useState('');

  useEffect(() => {
    loadHealthData();
    setGreetingMessage();
  }, []);

  const loadHealthData = async () => {
    try {
      const data = await AsyncStorage.getItem('healthData');
      if (data) {
        setHealthData(JSON.parse(data));
      }
    } catch (error) {
      console.log('Error loading health data:', error);
    }
  };

  const setGreetingMessage = () => {
    const hour = new Date().getHours();
    if (hour < 12) {
      setGreeting('Good Morning');
    } else if (hour < 18) {
      setGreeting('Good Afternoon');
    } else {
      setGreeting('Good Evening');
    }
  };

  const getHealthStatus = () => {
    const { heartRate, bloodPressure, mentalScore, sleepHours } = healthData;
    let alerts = 0;
    let warnings = [];

    if (heartRate && (heartRate < 60 || heartRate > 100)) {
      alerts++;
      warnings.push('Heart rate abnormal');
    }
    if (bloodPressure && (bloodPressure.systolic > 140 || bloodPressure.diastolic > 90)) {
      alerts++;
      warnings.push('Blood pressure elevated');
    }
    if (mentalScore && mentalScore < 3) {
      alerts++;
      warnings.push('Mental health needs attention');
    }
    if (sleepHours && sleepHours < 6) {
      alerts++;
      warnings.push('Insufficient sleep');
    }

    return { alerts, warnings };
  };

  const { alerts, warnings } = getHealthStatus();

  const handleEmergencyCall = () => {
    Alert.alert(
      'Emergency Call',
      'This will call emergency services. Continue?',
      [
        { text: 'Cancel', style: 'cancel' },
        { text: 'Call', style: 'destructive', onPress: () => {
          // In real app, this would make an actual emergency call
          Alert.alert('Emergency', 'Calling emergency services...');
        }},
      ]
    );
  };

  const MetricCard = ({ 
    title, 
    value, 
    unit, 
    icon: Icon, 
    color, 
    onPress 
  }: {
    title: string;
    value: string | number | null;
    unit?: string;
    icon: React.ComponentType<any>;
    color: string;
    onPress: () => void;
  }) => (
    <TouchableOpacity style={[styles.metricCard, { borderLeftColor: color }]} onPress={onPress}>
      <View style={styles.metricHeader}>
        <Icon size={24} color={color} />
        <Text style={styles.metricTitle}>{title}</Text>
      </View>
      <Text style={[styles.metricValue, { color }]}>
        {value !== null ? `${value}${unit || ''}` : 'No data'}
      </Text>
    </TouchableOpacity>
  );

  return (
    <ScrollView style={styles.container} showsVerticalScrollIndicator={false}>
      {/* Header */}
      <View style={styles.header}>
        <View>
          <Text style={styles.greeting}>{greeting}</Text>
          <Text style={styles.subtitle}>How are you feeling today?</Text>
        </View>
        <TouchableOpacity 
          style={styles.emergencyButton}
          onPress={handleEmergencyCall}
        >
          <Phone size={20} color="#FFFFFF" />
        </TouchableOpacity>
      </View>

      {/* Health Status Alert */}
      {alerts > 0 && (
        <View style={styles.alertCard}>
          <View style={styles.alertHeader}>
            <AlertTriangle size={24} color="#DC2626" />
            <Text style={styles.alertTitle}>Health Alert</Text>
          </View>
          <Text style={styles.alertText}>
            {alerts} metric(s) need attention:
          </Text>
          {warnings.map((warning, index) => (
            <Text key={index} style={styles.warningText}>
              • {warning}
            </Text>
          ))}
        </View>
      )}

      {/* Quick Stats */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Today's Overview</Text>
        <View style={styles.metricsGrid}>
          <MetricCard
            title="Heart Rate"
            value={healthData.heartRate}
            unit=" BPM"
            icon={Heart}
            color="#EF4444"
            onPress={() => router.push('/heart')}
          />
          <MetricCard
            title="Blood Pressure"
            value={
              healthData.bloodPressure
                ? `${healthData.bloodPressure.systolic}/${healthData.bloodPressure.diastolic}`
                : null
            }
            icon={Activity}
            color="#3B82F6"
            onPress={() => router.push('/heart')}
          />
          <MetricCard
            title="Mental Health"
            value={healthData.mentalScore}
            unit="/5"
            icon={Brain}
            color="#8B5CF6"
            onPress={() => router.push('/mental')}
          />
          <MetricCard
            title="Sleep"
            value={healthData.sleepHours}
            unit="h"
            icon={Moon}
            color="#10B981"
            onPress={() => router.push('/sleep')}
          />
        </View>
      </View>

      {/* Quick Actions */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Quick Actions</Text>
        <View style={styles.actionGrid}>
          <TouchableOpacity 
            style={styles.actionCard}
            onPress={() => router.push('/heart')}
          >
            <Heart size={32} color="#EF4444" />
            <Text style={styles.actionText}>Measure Heart Rate</Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={styles.actionCard}
            onPress={() => router.push('/mental')}
          >
            <Brain size={32} color="#8B5CF6" />
            <Text style={styles.actionText}>Mental Check</Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={styles.actionCard}
            onPress={() => router.push('/sleep')}
          >
            <Moon size={32} color="#10B981" />
            <Text style={styles.actionText}>Log Sleep</Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={styles.actionCard}
            onPress={() => Alert.alert('Coming Soon', 'Trends feature will be available soon!')}
          >
            <TrendingUp size={32} color="#F59E0B" />
            <Text style={styles.actionText}>View Trends</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* Health Tips */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Health Tips</Text>
        <View style={styles.tipCard}>
          <Calendar size={20} color="#6B7280" />
          <View style={styles.tipContent}>
            <Text style={styles.tipTitle}>Daily Wellness</Text>
            <Text style={styles.tipText}>
              Take 5 minutes for deep breathing exercises to reduce stress and improve focus.
            </Text>
          </View>
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 60,
    paddingBottom: 20,
    backgroundColor: '#FFFFFF',
  },
  greeting: {
    fontSize: 24,
    fontWeight: '700',
    color: '#1F2937',
  },
  subtitle: {
    fontSize: 16,
    color: '#6B7280',
    marginTop: 4,
  },
  emergencyButton: {
    backgroundColor: '#DC2626',
    width: 48,
    height: 48,
    borderRadius: 24,
    justifyContent: 'center',
    alignItems: 'center',
  },
  alertCard: {
    backgroundColor: '#FEF2F2',
    marginHorizontal: 20,
    marginVertical: 16,
    padding: 16,
    borderRadius: 12,
    borderLeftWidth: 4,
    borderLeftColor: '#DC2626',
  },
  alertHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  alertTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#DC2626',
    marginLeft: 8,
  },
  alertText: {
    fontSize: 14,
    color: '#374151',
    marginBottom: 4,
  },
  warningText: {
    fontSize: 14,
    color: '#DC2626',
    marginLeft: 12,
  },
  section: {
    paddingHorizontal: 20,
    marginVertical: 16,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    color: '#1F2937',
    marginBottom: 16,
  },
  metricsGrid: {
    gap: 12,
  },
  metricCard: {
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderRadius: 12,
    borderLeftWidth: 4,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  metricHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  metricTitle: {
    fontSize: 16,
    fontWeight: '500',
    color: '#374151',
    marginLeft: 8,
  },
  metricValue: {
    fontSize: 24,
    fontWeight: '700',
  },
  actionGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    gap: 12,
  },
  actionCard: {
    backgroundColor: '#FFFFFF',
    width: '48%',
    padding: 20,
    borderRadius: 12,
    alignItems: 'center',
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  actionText: {
    fontSize: 14,
    fontWeight: '500',
    color: '#374151',
    marginTop: 8,
    textAlign: 'center',
  },
  tipCard: {
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderRadius: 12,
    flexDirection: 'row',
    alignItems: 'flex-start',
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  tipContent: {
    flex: 1,
    marginLeft: 12,
  },
  tipTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#1F2937',
    marginBottom: 4,
  },
  tipText: {
    fontSize: 14,
    color: '#6B7280',
    lineHeight: 20,
  },
});
