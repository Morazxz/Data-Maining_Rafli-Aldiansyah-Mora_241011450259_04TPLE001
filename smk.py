from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
	from sklearn.impute import SimpleImputer
except ImportError:
	SimpleImputer = None


DATASET_PATH = Path(__file__).resolve().parent / "dataset_siswa_smk_kuliah_2500.csv"


def main():
	if not DATASET_PATH.exists():
		raise FileNotFoundError(f"Dataset tidak ditemukan: {DATASET_PATH}")

	# pandas digunakan untuk memuat dan mengelola data CSV.
	data = pd.read_csv(DATASET_PATH)
	categorical_columns = data.select_dtypes(
		include=["object", "category", "bool"]
	).columns.tolist()
	numerical_columns = data.select_dtypes(include=["number"]).columns.tolist()

	print("=== INFORMASI DATASET ===")
	print(f"Lokasi file       : {DATASET_PATH.name}")
	print(f"Jumlah baris      : {len(data)}")
	print(f"Jumlah kolom      : {len(data.columns)}")
	print(f"Ukuran dataset    : {data.shape}")
	print("\nContoh data:")
	print(data.head())

	print("\n=== JENIS KOLOM ===")
	print(f"Jumlah kolom kategorikal: {len(categorical_columns)}")
	print("Kolom kategorikal:")
	if categorical_columns:
		print(data[categorical_columns].nunique(dropna=False).rename("Jumlah nilai unik"))
	else:
		print("Tidak ada")

	print(f"\nJumlah kolom numerikal: {len(numerical_columns)}")
	print("Kolom numerikal:")
	if numerical_columns:
		print(data[numerical_columns].describe().T)
	else:
		print("Tidak ada")

	# NumPy menghitung nilai nol hanya pada kolom numerikal.
	if numerical_columns:
		numeric_data = data[numerical_columns]
		zero_counts = (numeric_data == 0).sum()
		total_zeros = int(np.count_nonzero(numeric_data.to_numpy() == 0))
	else:
		zero_counts = pd.Series(dtype="int64")
		total_zeros = 0

	null_counts = data.isna().sum()
	duplicate_count = int(data.duplicated().sum())

	print("\n=== PEMERIKSAAN KUALITAS DATA ===")
	print(f"Jumlah baris duplikat : {duplicate_count}")
	print(f"Jumlah seluruh nilai null: {int(null_counts.sum())}")
	print("Null per kolom:")
	print(null_counts[null_counts > 0] if null_counts.any() else "Tidak ada null")
	print(f"Jumlah seluruh nilai zero (kolom numerikal): {total_zeros}")
	print("Zero per kolom numerikal:")
	print(zero_counts[zero_counts > 0] if total_zeros else "Tidak ada zero")

	# sklearn mengisi null pada salinan data agar data asli dan hitungannya tetap utuh.
	cleaned_data = data.copy()
	numeric_to_impute = [
		column
		for column in numerical_columns
		if data[column].isna().any() and data[column].notna().any()
	]
	categorical_to_impute = [
		column
		for column in categorical_columns
		if data[column].isna().any() and data[column].notna().any()
	]
	if numeric_to_impute:
		if SimpleImputer is not None:
			numeric_imputer = SimpleImputer(strategy="median")
			cleaned_data[numeric_to_impute] = numeric_imputer.fit_transform(
				data[numeric_to_impute]
			)
		else:
			cleaned_data[numeric_to_impute] = data[numeric_to_impute].fillna(
				data[numeric_to_impute].median()
			)
	if categorical_to_impute:
		if SimpleImputer is not None:
			categorical_imputer = SimpleImputer(strategy="most_frequent")
			cleaned_data[categorical_to_impute] = categorical_imputer.fit_transform(
				data[categorical_to_impute]
			)
		else:
			for column in categorical_to_impute:
				most_frequent = data[column].mode(dropna=True)
				cleaned_data[column] = data[column].fillna(most_frequent.iloc[0])
	if SimpleImputer is None and (numeric_to_impute or categorical_to_impute):
		print("scikit-learn tidak tersedia; null diisi menggunakan pandas.")
	print(
		"\nJumlah nilai null yang terisi pada salinan data:",
		int(data.isna().sum().sum() - cleaned_data.isna().sum().sum()),
	)

	# matplotlib menampilkan ringkasan tipe kolom serta null dan zero per kolom.
	figure, axes = plt.subplots(2, 1, figsize=(12, 9))
	axes[0].bar(
		["Kategorikal", "Numerikal"],
		[len(categorical_columns), len(numerical_columns)],
		color=["#287271", "#e07a5f"],
	)
	axes[0].set_title("Jumlah Kolom Berdasarkan Jenis Data")
	axes[0].set_ylabel("Jumlah kolom")

	quality_counts = pd.DataFrame({"Null": null_counts})
	if numerical_columns:
		quality_counts["Zero"] = zero_counts.reindex(data.columns, fill_value=0)
	quality_counts.plot(kind="bar", ax=axes[1], color=["#e07a5f", "#3d5a80"][: len(quality_counts.columns)])
	axes[1].set_title("Jumlah Null dan Zero per Kolom")
	axes[1].set_ylabel("Jumlah nilai")
	axes[1].set_xlabel("Kolom")
	axes[1].tick_params(axis="x", rotation=45)

	figure.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
