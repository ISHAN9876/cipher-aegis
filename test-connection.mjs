import { createClient } from '@supabase/supabase-js';
import dns from 'dns';

// Force IPv4
dns.setDefaultResultOrder('ipv4first');

const supabaseUrl = 'https://ppwjjppfhkgtyfnehosb.supabase.co';
const supabaseKey = 'sb_publishable_RhQ5JnJvS8Xngh7mDW6U-Q_HPEEM_M4'; // Use the service_role key

const supabase = createClient(supabaseUrl, supabaseKey, {
  fetchOptions: {
    timeout: 10000,
  },
});

async function testConnection() {
  try {
    console.log('Testing connection to Supabase (IPv4)...');
    const { data, error } = await supabase
      .from('wallpapers')
      .select('*')
      .limit(1);

    if (error) throw error;
    console.log('Success! Data:', data);
  } catch (error) {
    console.error('Error:', error);
  }
}

testConnection();

