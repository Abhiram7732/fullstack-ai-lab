import { ClerkProvider } from '@clerk/nextjs';
import type { AppProps } from 'next/app';
import '../styles/globals.css';

import { dark } from '@clerk/themes';  

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ClerkProvider {...pageProps}
      appearance={{
        variables: {
          colorPrimary: '#8b5cf6',
          colorBackground: '#17122b',
          colorText: '#ede9fe',
          colorTextSecondary: '#9a94b8',
          colorInputBackground: '#0a0714',
          colorInputText: '#ede9fe',
          colorNeutral: '#ffffff',
          colorTextOnPrimaryBackground: '#ffffff',
          borderRadius: '0.75rem',
        },
      }}
    >
      <Component {...pageProps} />
    </ClerkProvider>
  );
}