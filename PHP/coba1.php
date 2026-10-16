<?php
$harga = 250000; 
$qty = 1;
$diskon = 0.15;

$total = $harga * $qty;
$bayar = $total - ($total * $diskon);
$ongkir = $bayar>= 500000 ? "Gratis" :"Rp 20.000";
$pajak = $bayar*0.10;
$totalAkhir = $bayar + $pajak;

echo "total belanja = Rp ".number_format($total) . "\n";
echo "setelah diskon = Rp ".number_format($bayar) . "\n";
echo "ongkir = " .$ongkir . "\n";
echo "pajak 10% = Rp " .number_format($pajak). "\n";
echo "total akhir = Rp " .number_format($totalAkhir);