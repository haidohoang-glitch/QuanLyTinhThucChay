# Stored Procedure: `ThucChay_PR_ThucChayDaTinh_DEV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-24 09:39:08.210000
- **Ngày sửa cuối**: 2025-10-24 09:39:08.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[ThucChay_PR_ThucChayDaTinh_DEV]
    @NgayGhiNhan DATE,
	@NgayCheckThayDoi DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL
AS
    BEGIN
        DECLARE @xulytay NVARCHAR(50)
		SET @xulytay = N''
		IF @SoHopDong IS NOT NULL 
		BEGIN
			SET @xulytay = N'xử lý tay '
			SET @NgayCheckThayDoi = NULL
			SET @NgayDanhSoGioiHan = NULL
		END


		CREATE TABLE #DmThayDoi 
		( ThucChayHopDongChiTietID INT,
		  HopDongChiTietID INT,
		  HopDongChitiet_BF INT,
		  HopDongREF INT ,
		  DmNhanHangREF INT,
		  DmChuyenMucREF INT,
		  TenChuyenMucREF NVARCHAR(100),
		  NgayThucHien DATETIME,
		  WebsiteREF FLOAT,
		  TenWebsite NVARCHAR(50),
		  RecordStatus INT,
		  DonGiaTreo FLOAT,
		  ChietKhauTreo FLOAT,
		  SoLuong INT,
		  ChietKhauHDCT FLOAT,

		  ThanhTienKhuyenMaiTreo FLOAT,
		  ThanhTienSauCKTreo FLOAT,
		  ThanhTienKhuyenMaiPhanBo FLOAT,
		  ThanhTienSauCKPhanBo FLOAT,
		  ThanhTienKhuyenMaiDaTinh FLOAT,
		  ThanhTienSauCKDaTinh FLOAT,
		  LoaiThayDoi INT,  
		  LyDo NVARCHAR(MAX),
		  LoaiXuLy INT, -- 0: không xử lý, 1: đối trừ, 2: đối từ tính lại, 3: ghi nhận mới

		  LastModifiedTreo DATE
		)


		DELETE
		FROM ABM_data_thucchay.dbo.ThucChayDaTinh 
		WHERE   NgayThucHien = @NgayGhiNhan
                AND DotChayHopDong LIKE N'ThucChay_PR'
				AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
				AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)
        --=================================================== 1: Xác định danh mục ID cần đối trừ hoặc ghi nhận thêm ====================================
		/* TH1 phân bổ hoặc hợp đồng xóa, hủy hoặc ID treo hủy: đối trừ toàn bộ các ID treo liên quan đã được ghi nhận thực chạy
		   TH2 phân bổ thay đổi giá trị, thuộc tính : với mỗi phân bổ sắp xếp toàn bộ ID treo theo thứ tự RecordStatus 1->0, ID asc
		       Nếu vượt thì đối trừ với ID treo đã tính
			   Nếu không vượt thì đối trừ tính lại với ID treo đã tính và tính mới cho ID chưa tính
		   TH3 ID treo thay đổi giá trị/ phân bổ hoặc ID treo thêm mới: với mỗi phân bổ sắp xếp ID treo theo thứ tự RecordStatus 1->0, ID treo asc
		       Nếu không vượt thì ghi nhận mới hoặc đối trừ tính lại với ID treo đã ghi nhận
			   Nếu vượt thì đối trừ với ID treo đã tính
		   TH4 phân bổ hoặc ID treo thay đổi thuộc tính mà ID treo không nằm trong danh sách trên: ghi nhận âm cho thuộc tính cũ và dương cho thuộc tính mới
		   TH5 xử lý tay, không quan tâm đến các điều kiện trên: với mỗi phân bổ sắp xếp ID treo theo thứ tự RecordStatus 1->0, ID treo asc
		       Nếu không vượt thì ghi nhận mới hoặc đối trừ tính lại với ID treo đã ghi nhận
			   Nếu vượt thì đối trừ với ID treo đã tính
		*/
		BEGIN
			INSERT INTO #DmThayDoi
			(   ThucChayHopDongChiTietID ,
				HopDongChiTietID ,
				HopDongREF  ,
				DmNhanHangREF ,
				DmChuyenMucREF ,
				TenChuyenMucREF ,
				NgayThucHien ,
				WebsiteREF ,
				TenWebsite,
				RecordStatus ,
				DonGiaTreo ,
				ChietKhauTreo ,
				SoLuong ,
				ChietKhauHDCT ,

				ThanhTienKhuyenMaiTreo ,
				ThanhTienSauCKTreo ,
				ThanhTienKhuyenMaiPhanBo ,
				ThanhTienSauCKPhanBo ,
				ThanhTienKhuyenMaiDaTinh ,
				ThanhTienSauCKDaTinh ,
				LoaiThayDoi ,  
				LyDo ,
				LoaiXuLy,

				LastModifiedTreo
			)
			SELECT  DISTINCT
					tchdct.ThucChayHopDongChiTietPRID,
					tchdct.HopDongChiTietREF ,
					hd.HopDongID ,
					DmNhanHangREF ,
					DmChuyenMucREF = NULL,
					TenChuyenMucREF = NULL,
					@NgayGhiNhan,
					WebsiteREF = NULL,
					TenWebsite = NULL,
					RecordStatus = NULL,
					DonGiaTreo = NULL,
					ChietKhauTreo = NULL,
					SoLuong = NULL,
					ChietKhauHDCT = NULL,

					ThanhTienKhuyenMaiTreo = NULL,
					ThanhTienSauCKTreo = NULL,
					ThanhTienKhuyenMaiPhanBo = NULL,
					ThanhTienSauCKPhanBo = NULL,
					ThanhTienKhuyenMaiDaTinh = NULL,
					ThanhTienSauCKDaTinh = NULL,
					LoaiThayDoi = 1,
					LyDo =	N'hợp đồng xóa, hủy hoặc hủy phân bổ hoặc ID treo hủy',
					LoaiXuLy = 1,   -- đối trừ treo ID

					LastModifiedTreo = CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt))
			FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  tchdct.RecordStatus = 1 
				   AND (
						((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND 
						 CONVERT(DATE, ISNULL(hd.LastModifiedAt, hd.CreatedAt))  = @NgayCheckThayDoi) OR
						(hdct.DeletedStatus = 1 AND 
						 CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi) OR
						(tchdct.DeletedStatus = 1 AND CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
					   )
				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND @xulytay = ''
			
			INSERT INTO #DmThayDoi
			(   ThucChayHopDongChiTietID ,
				HopDongChiTietID ,
				HopDongREF  ,
				DmNhanHangREF ,
				DmChuyenMucREF ,
				TenChuyenMucREF ,
				NgayThucHien ,
				WebsiteREF ,
				TenWebsite,
				RecordStatus ,
				DonGiaTreo ,
				ChietKhauTreo ,
				SoLuong ,
				ChietKhauHDCT ,

				ThanhTienKhuyenMaiTreo ,
				ThanhTienSauCKTreo ,
				ThanhTienKhuyenMaiPhanBo ,
				ThanhTienSauCKPhanBo ,
				ThanhTienKhuyenMaiDaTinh ,
				ThanhTienSauCKDaTinh ,
				LoaiThayDoi ,  
				LyDo ,
				LoaiXuLy,

				LastModifiedTreo
			)
			SELECT  DISTINCT
					tchdct.ThucChayHopDongChiTietPRID,
					tchdct.HopDongChiTietREF ,
					hd.HopDongID ,
					DmNhanHangREF = tchdct.DmNhanHangREF,
					DmChuyenMucREF = tchdct.DmChuyenMucREF,
					TenChuyenMucREF = tchdct.TenChuyenMuc,
					@NgayGhiNhan,
					WebsiteREF = tchdct.DmWebsiteREF,
				    TenWebsite = tchdct.TenWebsite,
					RecordStatus = tchdct.RecordStatus,
					DonGiaTreo = tchdct.GiaTien,
					ChietKhauTreo = tchdct.ChietKhau,
					SoLuong = tchdct.SoLuong,
					ChietKhauHDCT = hdct.ChietKhau,

					ThanhTienKhuyenMaiTreo = IIF(tchdct.ChietKhau = 100 AND hdct.ChietKhau = 100, tchdct.GiaTien*tchdct.SoLuong, 0),
					ThanhTienSauCKTreo = IIF(tchdct.ChietKhau <> 100 AND hdct.ChietKhau <> 100, tchdct.GiaTien*tchdct.SoLuong*(1-tchdct.ChietKhau/100), 0),
					ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100, hdct.DonGia*hdct.SoLuong, 0),
					ThanhTienSauCKPhanBo = hdct.DonGia*hdct.SoLuong*(1-hdct.ChietKhau/100),
					ThanhTienKhuyenMaiDaTinh = 0,
					ThanhTienSauCKDaTinh = 0,
					LoaiThayDoi = 2 ,
					LyDo =	N'phân bổ thay đổi thành tiền sau CK/thành tiền KM/HTQC/SP hoặc hợp đồng thay đổi ngày đánh số/sale/tên login' ,
					LoaiXuLy = NULL,

					LastModifiedTreo = CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt))
			FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE   hdct.DeletedStatus = 0 AND hd.TrangThaiHopDong <> 3 AND tchdct.DeletedStatus = 0 AND
					(CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi OR 
					 CONVERT(DATE, ISNULL(hd.LastModifiedAt, hd.CreatedAt)) = @NgayCheckThayDoi) AND 
					(@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND 
					@xulytay = '' AND 
					tchdct.ThucChayHopDongChiTietPRID NOT IN (SELECT ThucChayHopDongChiTietID FROM #DmThayDoi) AND 
					IIF(tchdct.RecordStatus = 0, tchdct.ThoiGianBatDau, '2019-01-01') >= '2019-01-01'
                 

			DELETE dm
			FROM #DmThayDoi dm
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = dm.HopDongREF
			OUTER APPLY (SELECT TOP 1 ThanhTienKhuyenMaiPhanBo = IIF(l.ChietKhau = 100, l.DonGia*l.ChietKhau, 0),
									  ThanhTienSauCKPhanBo = l.DonGia*l.ChietKhau*(1-l.ChietKhau/100),
									  l.IsKhuyenMai,
									  l.DmLoaiREF,
									  l.DmSanPhamREF
			             FROM ABM_data_thucchay.dbo.HopDongChiTietLog l
						 WHERE l.HopDongChiTietREF = hdct.HopDongChiTietID AND 
						       l.LastModifiedAt < @NgayCheckThayDoi
						 ORDER BY l.LastModifiedAt desc) l
			OUTER APPLY (SELECT TOP 1 hdl.SoHopDong, hdl.NgayDanhSoHopDong, hdl.SysNhanVienREF, hdl.DmMaHopDongREF, hdl.TenDangNhap
			             FROM ABM_data_thucchay.dbo.HopDongLog hdl
						 WHERE hdl.HopDongID = hd.hopdongID AND 
						       hdl.LastModifiedAt < @NgayCheckThayDoi
						 ORDER BY hdl.LastModifiedAt desc) hdl
			WHERE dm.ThanhTienKhuyenMaiPhanBo = ISNULL(l.ThanhTienKhuyenMaiPhanBo, dm.ThanhTienKhuyenMaiPhanBo) AND
                  dm.ThanhTienSauCKPhanBo = ISNULL(l.ThanhTienSauCKPhanBo,  dm.ThanhTienSauCKPhanBo) AND
				  hdct.IsKhuyenMai = ISNULL(l.IsKhuyenMai, hdct.IsKhuyenMai) AND 
				  hdct.DmLoaiREF = ISNULL(l.DmLoaiREF, hdct.DmLoaiREF) AND 
				  hdct.DmSanPhamREF = ISNULL(l.DmSanPhamREF, hdct.DmSanPhamREF) AND
                  hd.SoHopDong = ISNULL(hdl.SoHopDong, hd.SoHopDong) AND 
				  hd.NgayDanhSoHopDong = ISNULL(hdl.NgayDanhSoHopDong, hd.NgayDanhSoHopDong) AND 
				  hd.SysNhanVienREF = ISNULL(hdl.SysNhanVienREF, hd.SysNhanVienREF) AND 
				  hd.DmMaHopDongREF = ISNULL(hdl.DmMaHopDongREF, hd.DmMaHopDongREF) AND 
				  hd.TenDangNhap = ISNULL(hdl.TenDangNhap, hd.TenDangNhap) AND 
                  dm.LoaiThayDoi = 2

			INSERT INTO #DmThayDoi
			(   ThucChayHopDongChiTietID ,
				HopDongChiTietID ,
				HopDongREF  ,
				DmNhanHangREF ,
				DmChuyenMucREF ,
				TenChuyenMucREF ,
				NgayThucHien ,
				WebsiteREF,
				TenWebsite ,
				RecordStatus ,
				DonGiaTreo ,
				ChietKhauTreo ,
				SoLuong ,
				ChietKhauHDCT ,

				ThanhTienKhuyenMaiTreo ,
				ThanhTienSauCKTreo ,
				ThanhTienKhuyenMaiPhanBo ,
				ThanhTienSauCKPhanBo ,
				ThanhTienKhuyenMaiDaTinh ,
				ThanhTienSauCKDaTinh ,
				LoaiThayDoi ,  
				LyDo ,
				LoaiXuLy,

				LastModifiedTreo 
			)
			SELECT  DISTINCT
					tchdct.ThucChayHopDongChiTietPRID,
					tchdct.HopDongChiTietREF ,
					hd.HopDongID ,
					DmNhanHangREF = tchdct.DmNhanHangREF,
					DmChuyenMucREF = tchdct.DmChuyenMucREF,
					TenChuyenMucREF = tchdct.TenChuyenMuc,
					@NgayGhiNhan,
					WebsiteREF = tchdct.DmWebsiteREF,
				    TenWebsite = tchdct.TenWebsite,
					RecordStatus = tchdct.RecordStatus,
					DonGiaTreo = tchdct.GiaTien,
					ChietKhauTreo = tchdct.ChietKhau,
					SoLuong = tchdct.SoLuong,
					ChietKhauHDCT = hdct.ChietKhau,

					ThanhTienKhuyenMaiTreo = IIF(tchdct.ChietKhau = 100 AND hdct.ChietKhau = 100, tchdct.GiaTien*tchdct.SoLuong, 0),
					ThanhTienSauCKTreo = IIF(tchdct.ChietKhau <> 100 AND hdct.ChietKhau <> 100, tchdct.GiaTien*tchdct.SoLuong*(1-tchdct.ChietKhau/100), 0),
					ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100, hdct.DonGia*hdct.SoLuong, 0),
					ThanhTienSauCKPhanBo = hdct.DonGia*hdct.SoLuong*(1-hdct.ChietKhau/100),
					ThanhTienKhuyenMaiDaTinh = NULL,
					ThanhTienSauCKDaTinh = NULL,
					LoaiThayDoi = CASE WHEN tchdct.RecordStatus = 1 THEN 3
					                   WHEN tchdct.RecordStatus = 0 THEN 4
								  END ,
					LyDo =	CASE WHEN tchdct.RecordStatus = 1 THEN N'treo thay đổi dongia/soluong/chiêtkhau/phân bổ gán/nhãn/website'
					             WHEN tchdct.RecordStatus = 0 THEN N'treo thêm mới'
								 END ,
					LoaiXuLy = NULL,

					LastModifiedTreo = CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt))
			FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE   tchdct.DeletedStatus = 0 AND hd.TrangThaiHopDong <> 3 AND hdct.DeletedStatus = 0 AND 
					((CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi and tchdct.RecordStatus = 1) OR
					 (CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) <= @NgayCheckThayDoi and tchdct.RecordStatus = 0))    AND 
					tchdct.ThucChayHopDongChiTietPRID NOT IN ( SELECT ThucChayHopDongChiTietID FROM #DmThayDoi) AND
					(@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND 
					IIF(tchdct.RecordStatus = 0, tchdct.ThoiGianBatDau, '2019-01-01') >= '2019-01-01' AND 
					@xulytay = ''

			DELETE dm
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT TOP 1 l.GiaTien, l.SoLuong, l.ChietKhau, l.HopDongChiTietREF, l.DmNhanHangREF, l.DmWebsiteREF
						 FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTietPRLog l
						 WHERE l.ThucChayHopDongChiTietPRREF = dm.ThucChayHopDongChiTietID AND 
						       l.LastModifiedAt < @NgayCheckThayDoi
						 ORDER BY l.LastModifiedAt DESC ) l
			WHERE dm.LoaiThayDoi = 3 AND 
			      dm.dongiatreo = ISNULL(l.GiaTien, dm.dongiatreo) AND
				  dm.SoLuong = ISNULL(l.SoLuong, dm.SoLuong) AND
                  dm.ChietKhauTreo = ISNULL(l.ChietKhau, dm.ChietKhauTreo) AND
				  dm.HopDongChiTietID = ISNULL(l.HopDongChiTietREF, dm.HopDongChiTietID) AND 
				  dm.DmNhanHangREF = ISNULL(l.DmNhanHangREF, dm.DmNhanHangREF) AND 
				  dm.WebsiteREF = ISNULL(l.DmWebsiteREF, dm.WebsiteREF)  

			UPDATE dm
			SET dm.HopDongChitiet_BF = ISNULL(l.HopDongChiTietREF, dm.HopDongChiTietID)
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT TOP 1 l.HopDongChiTietREF
						 FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTietPRLog l
						 WHERE l.ThucChayHopDongChiTietPRREF = dm.ThucChayHopDongChiTietID AND 
						       l.LastModifiedAt < @NgayGhiNhan
						 ORDER BY l.LastModifiedAt DESC ) l
			WHERE LastModifiedTreo = @NgayGhiNhan

			UPDATE dm
			SET dm.HopDongChitiet_BF = dm.HopDongChiTietID
			FROM #DmThayDoi dm
			WHERE LastModifiedTreo <> @NgayGhiNhan


			IF @xulytay = N'xử lý tay ' 
			BEGIN
				INSERT INTO #DmThayDoi
				(   ThucChayHopDongChiTietID ,
					HopDongChiTietID ,
					HopDongChitiet_BF,
					HopDongREF  ,
					DmNhanHangREF ,
					DmChuyenMucREF ,
					TenChuyenMucREF ,
					NgayThucHien ,
					WebsiteREF,
					TenWebsite ,
					RecordStatus ,
					DonGiaTreo ,
					ChietKhauTreo ,
					SoLuong ,
					ChietKhauHDCT ,

					ThanhTienKhuyenMaiTreo ,
					ThanhTienSauCKTreo ,
					ThanhTienKhuyenMaiPhanBo ,
					ThanhTienSauCKPhanBo ,
					ThanhTienKhuyenMaiDaTinh ,
					ThanhTienSauCKDaTinh ,
					LoaiThayDoi ,  
					LyDo ,
					LoaiXuLy,

					LastModifiedTreo 
				)
				SELECT  DISTINCT
						tchdct.ThucChayHopDongChiTietPRID,
						tchdct.HopDongChiTietREF ,
						tchdct.HopDongChiTietREF ,   -- TH xử lý tay, truyền vào phân bổ nào, xử lý riêng phân bổ đó, nên với TH treo đổi phân bổ từ A -> B, sẽ cần xử lý tay 2 phân bổ A và B
						hd.HopDongID ,
						DmNhanHangREF = tchdct.DmNhanHangREF,
						DmChuyenMucREF = tchdct.DmChuyenMucREF,
						TenChuyenMucREF = tchdct.TenChuyenMuc,
						@NgayGhiNhan,
						WebsiteREF = tchdct.DmWebsiteREF,
						TenWebsite = tchdct.TenWebsite,
						RecordStatus = tchdct.RecordStatus,
						DonGiaTreo = tchdct.GiaTien,
						ChietKhauTreo = tchdct.ChietKhau,
						SoLuong = tchdct.SoLuong,
						ChietKhauHDCT = hdct.ChietKhau,

						ThanhTienKhuyenMaiTreo = IIF(tchdct.ChietKhau = 100 AND hdct.ChietKhau = 100, tchdct.GiaTien*tchdct.SoLuong, 0),
						ThanhTienSauCKTreo = IIF(tchdct.ChietKhau <> 100 AND hdct.ChietKhau <> 100, tchdct.GiaTien*tchdct.SoLuong*(1-tchdct.ChietKhau/100), 0),
						ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100, hdct.DonGia*hdct.SoLuong, 0),
						ThanhTienSauCKPhanBo = hdct.DonGia*hdct.SoLuong*(1-hdct.ChietKhau/100),
						ThanhTienKhuyenMaiDaTinh = NULL,
						ThanhTienSauCKDaTinh = NULL,
						LoaiThayDoi = CASE WHEN hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1 OR hdct.DeletedStatus = 1 THEN 1
										   WHEN tchdct.RecordStatus = 1 AND tchdct.DeletedStatus = 1 THEN 1
										   WHEN  tchdct.RecordStatus = 1 AND tchdct.DeletedStatus = 0 THEN 3
										   WHEN tchdct.RecordStatus = 0 AND tchdct.DeletedStatus = 0 THEN 4
									  END ,
						LyDo =	CASE WHEN tchdct.RecordStatus = 1 THEN @xulytay + N'phân bổ'
									 WHEN tchdct.RecordStatus = 0 THEN @xulytay + N'phân bổ'
									 END ,
						LoaiXuLy = IIF( hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1 OR hdct.DeletedStatus = 1, 1, NULL),

						LastModifiedTreo = CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt))
				FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct
				INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
				INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				WHERE   tchdct.ThucChayHopDongChiTietPRID NOT IN ( SELECT ThucChayHopDongChiTietID FROM #DmThayDoi) AND
						IIF(tchdct.RecordStatus = 0, tchdct.ThoiGianBatDau, '2019-01-01') >= '2019-01-01'  AND 
						hd.SoHopDong = @SoHopDong AND 
					   (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			END


			UPDATE dm
			SET 	WebsiteREF = ABM_data_thucchay.dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(dm.WebsiteREF),
					TenWebsite = ABM_data_thucchay.dbo.GetWebsiteLinkByDmWebsiteID(dm.WebsiteREF, dm.TenWebsite)
			FROM #DmThayDoi dm
			WHERE LoaiThayDoi  IN (2,3,4)

			UPDATE dm
			SET dm.ThanhTienKhuyenMaiDaTinh = ISNULL(tchdct.ThanhTienKhuyenMaiDaTinh,0),
			    dm.ThanhTienSauCKDaTinh = ISNULL(tchdct.ThanhTienSauCKDaTinh,0)
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT ThanhTienKhuyenMaiDaTinh = SUM (IIF(tchdct.ChietKhau = 100,tchdct.SoLuong*tchdct.GiaTien, 0)),
			                    ThanhTienSauCKDaTinh =  SUM(tchdct.SoLuong*tchdct.GiaTien*(1-tchdct.ChietKhau/100))
						 FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct
						 WHERE dm.HopDongChiTietID = tchdct.HopDongChiTietREF AND
						       tchdct.ThucChayHopDongChiTietPRID NOT IN (SELECT ThucChayHopDongChiTietID FROM #DmThayDoi) AND
							   tchdct.RecordStatus = 1 AND tchdct.DeletedStatus = 0
						 ) tchdct
			WHERE dm.LoaiThayDoi IN (3,4)


		END
		--=================================================== 2: Xác định phương thức xử lý cho ID treo thuộc: LoaiThayDoi in (2,3,4) ===========
		-- 0: không xử lý, 1: đối trừ, 2: đối trừ tính lại, 3: ghi nhận mới
		BEGIN 
			;WITH CTE_Base AS (
				SELECT 
					ThucChayHopDongChiTietID,
					RecordStatus,
					ThanhTienKhuyenMaiTreo,
					ThanhTienSauCKTreo,
					ThanhTienKhuyenMaiDaTinh,
					ThanhTienSauCKDaTinh,
					ThanhTienKhuyenMaiPhanBo,
					ThanhTienSauCKPhanBo,
					HopDongChiTietID,
					ROW_NUMBER() OVER (PARTITION BY HopDongChiTietID ORDER BY RecordStatus DESC, LastModifiedTreo DESC, ThucChayHopDongChiTietID ASC ) AS RowNum
				FROM #DmThayDoi
				WHERE LoaiThayDoi IN (2,3,4) ),

			 CTE_Recursive AS (
				SELECT 
					ThucChayHopDongChiTietID,
					RecordStatus,
					ThanhTienKhuyenMaiTreo,
					ThanhTienSauCKTreo,
					ThanhTienKhuyenMaiDaTinh,
					ThanhTienSauCKDaTinh,
					ThanhTienKhuyenMaiPhanBo,
					ThanhTienSauCKPhanBo,
					HopDongChiTietID,
					RowNum,
					TichLuyThanhTienKM = IIF (ROUND(ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo, 0) > ROUND(ThanhTienKhuyenMaiPhanBo, 0),
					                          ThanhTienKhuyenMaiDaTinh, 
											  ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (ROUND(ThanhTienSauCKDaTinh + ThanhTienSauCKTreo, 0) > ROUND(ThanhTienSauCKPhanBo, 0),
												 ThanhTienSauCKDaTinh, 
												 ThanhTienSauCKDaTinh + ThanhTienSauCKTreo ),
					GhiNhanKM = IIF(ROUND(ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo, 0) > ROUND(ThanhTienKhuyenMaiPhanBo, 0),
					                0, ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (ROUND(ThanhTienSauCKDaTinh + ThanhTienSauCKTreo, 0) > ROUND(ThanhTienSauCKPhanBo, 0),
												 0, ThanhTienSauCKTreo )
				FROM CTE_Base
				WHERE RowNum = 1

				UNION ALL
				-- Tính toán đệ quy
				SELECT 
					b.ThucChayHopDongChiTietID,
					b.RecordStatus,
					b.ThanhTienKhuyenMaiTreo,
					b.ThanhTienSauCKTreo,
					b.ThanhTienKhuyenMaiDaTinh,
					b.ThanhTienSauCKDaTinh,
					b.ThanhTienKhuyenMaiPhanBo,
					b.ThanhTienSauCKPhanBo,
					b.HopDongChiTietID,
					b.RowNum,
					TichLuyThanhTienKM = IIF (ROUND(r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo, 0) > ROUND(b.ThanhTienKhuyenMaiPhanBo, 0),
					                          r.TichLuyThanhTienKM, 
											  r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (ROUND(r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo, 0) > ROUND(b.ThanhTienSauCKPhanBo, 0),
												 r.TichLuyThanhTienSauCK, 
												 r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo ),
					GhiNhanKM =	IIF (ROUND(r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo, 0) > ROUND(b.ThanhTienKhuyenMaiPhanBo, 0),
									 0, b.ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (ROUND(r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo, 0) > ROUND(b.ThanhTienSauCKPhanBo, 0),
												 0, b.ThanhTienSauCKTreo )
				FROM CTE_Base b 
				INNER JOIN CTE_Recursive r  ON r.HopDongChiTietID = b.HopDongChiTietID AND r.RowNum = b.RowNum - 1
			)

			UPDATE dm
			SET dm.LoaiXuLy = CASE WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 1 
								   THEN 1
								   WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 0 
								   THEN 0
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 1 
								   THEN 2
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 0 
								   THEN 3
								   ELSE 0
							  END
			FROM #DmThayDoi dm
			INNER JOIN CTE_Recursive cte ON cte.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID
			WHERE dm.LoaiThayDoi IN (2,3,4)
			OPTION (MAXRECURSION 0);

			END 
		--=================================================== 2: Đối trừ thực chạy =============================================
		DECLARE @InsertedIDs TABLE (IDTreo NVARCHAR(100));

		INSERT INTO ABM_data_thucchay.dbo.ThucChayDaTinh
				([ThucChayDaTinhID]
				,[HopDongID]
				,[SoHopDong]
				,[DmMaHopDongREF]
				,[TenMaHopDong]
				,[NgayDanhSoHopDong]
				,[NgayKyHopDong]
				,[NhanHopDong]
				,[NgayNhanBanFax]
				,[NgayNhanHopDongBanCung]
				,[NgayChuyenHopDongChoKeToan]
				,[So]
				,[Thang]
				,[Nam]
				,[GiaTriHopDong]
				,[CongNo]
				,[HopDongChiTietREF]
				,[DangSuDung]
				,[IsGiayPhep]
				,[TrangThaiHopDong]
				,[IsBanCung]
				,[DmPhongBanREF]
				,[TenPhongBan]
				,[DmBoPhanREF]
				,[TenBoPhan]
				,[DmNhomLamViecREF]
				,[TenNhomLamViec]
				,[DmDiaDiemLamViecREF]
				,[TenDiaDiemLamViec]
				,[SysNhanVienREF]
				,[TenDangNhap]
				,[TenNhanVien]
				,[TenKhachHang]
				,[NhanHang]
				,[DmNhomNganhREF]
				,[TenNhomNganh]
				,[DmHinhThucQuangCao]
				,[TenHinhThucQuangCao]
				,[DmSanPhamREF]
				,[TenSanPham]
				,[DmNhomWebsiteREF]
				,[TenNhomWebsite]
				,[DmChuyenMucREF]
				,[TenChuyenMuc]
				,[DmLoaiBannerREF]
				,[TenLoaiBanner]
				,[DmViTriREF]
				,[TenViTri]
				,[DotChayHopDong]
				,[SoLuongDotChayHD]
				,[DotChayBooking]
				,[SoLuongDotChayBooking]
				,[SoLuong]
				,[DonViTinh]
				,[DonGia]
				,[DonGiaTheoDonVi]
				,[ChietKhau]
				,[GiamGia]
				,[ThanhTien]
				,[TiLeTuVan]
				,[ChiPhiTuVan]
				,[IsKhuyenMai]
				,[KhuyenMai]
				,[DmBannerREF]
				,[DmChienDichREF]
				,[DmWebsiteREF]
				,[TenWebsite]
				,[TongViewThucChay]
				,[TongClickThucChay]
				,[TongSoBaiViet]
				,[SoLuongThucChay]
				,[GiaTriThayDoi]
				,[ThanhTienThucChayTruocTrietKhau]
				,[GiaTriTrietKhauThucChay]
				,[ThanhTienSauTrietKhauThucChay]
				,[GiaTriHoaHongThucChay]
				,[ThanhTienThucThu]
				,[ThanhTienKM]
				,[SoLuongThucChayKM]
				,[SoLuongThucChayLechTreoHa]
				,[ThanhTienLechTreoHa]
				,[CreatedAt]
				,[LastModifiedAt]
				,[IsPheDuyet]
				,[PheDuyetBy]
				,[PheDuyetAt]
				,[SoLuongThayDoi]
				,[SoLuongKMThayDoi]
				,[GiaTriKMThayDoi]
				,[GhiChu]
				,[NgayThucHien])
		OUTPUT INSERTED.DotChayBooking INTO @InsertedIDs
		SELECT   NEWID() 
				,[HopDongID]
				,[SoHopDong]
				,[DmMaHopDongREF]
				,[TenMaHopDong]
				,[NgayDanhSoHopDong]
				,[NgayKyHopDong]
				,[NhanHopDong]
				,[NgayNhanBanFax]
				,[NgayNhanHopDongBanCung]
				,[NgayChuyenHopDongChoKeToan]
				,[So]
				,[Thang]
				,[Nam]
				,[GiaTriHopDong]
				,[CongNo]
				,[HopDongChiTietREF]
				,[DangSuDung]
				,[IsGiayPhep]
				,[TrangThaiHopDong]
				,[IsBanCung]
				,[DmPhongBanREF]
				,[TenPhongBan]
				,[DmBoPhanREF]
				,[TenBoPhan]
				,[DmNhomLamViecREF]
				,[TenNhomLamViec]
				,[DmDiaDiemLamViecREF]
				,[TenDiaDiemLamViec]
				,[SysNhanVienREF]
				,[TenDangNhap]
				,[TenNhanVien]
				,[TenKhachHang]
				,tcdt.[NhanHang]
				,tcdt.[DmNhomNganhREF]
				,tcdt.[TenNhomNganh]
				,[DmHinhThucQuangCao]
				,[TenHinhThucQuangCao]
				,tcdt.[DmSanPhamREF]
				,tcdt.[TenSanPham]
				,tcdt.[DmNhomWebsiteREF]
				,tcdt.[TenNhomWebsite]
				,tcdt.[DmChuyenMucREF]
				,tcdt.[TenChuyenMuc]
				,tcdt.[DmLoaiBannerREF]
				,tcdt.[TenLoaiBanner]
				,tcdt.[DmViTriREF]
				,tcdt.[TenViTri]
				,N'ThucChay_PR'
				,[SoLuongDotChayHD]
				,tcdt.DotChayBooking
				,[SoLuongDotChayBooking]
				,tcdt.[SoLuong]
				,tcdt.[DonViTinh]
				,tcdt.[DonGia]
				,[DonGiaTheoDonVi]
				,tcdt.[ChietKhau]
				,tcdt.[GiamGia]
				,tcdt.[ThanhTien]
				,tcdt.[TiLeTuVan]
				,tcdt.[ChiPhiTuVan]
				,tcdt.[IsKhuyenMai]
				,tcdt.[KhuyenMai]
				,tcdt.[DmBannerREF]
				,[DmChienDichREF]
				,tcdt.[DmWebsiteREF]
				,tcdt.[TenWebsite]
				,[TongViewThucChay]
				,[TongClickThucChay]
				,[TongSoBaiViet]
				,0 AS [SoLuongThucChay]
				,-SUM([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) AS [GiaTriThayDoi]
				,-SUM([ThanhTienThucChayTruocTrietKhau]) AS [ThanhTienThucChayTruocTrietKhau]
				,-SUM([GiaTriTrietKhauThucChay]) AS [GiaTriTrietKhauThucChay]
				,0 AS [ThanhTienSauTrietKhauThucChay]
				,0 AS [GiaTriHoaHongThucChay]
				,0 AS [ThanhTienThucThu]
				,0 AS [ThanhTienKM]
				,0 AS [SoLuongThucChayKM]
				,0 AS [SoLuongThucChayLechTreoHa]
				,0 AS [ThanhTienLechTreoHa]
				,GETDATE() AS [CreatedAt]
				,GETDATE() AS [LastModifiedAt]
				,0 AS [IsPheDuyet]
				,'' AS [PheDuyetBy]
				,'' AS [PheDuyetAt]
				,-SUM(tcdt.[SoLuongThucChay] + tcdt.[SoLuongThayDoi]) AS [SoLuongThayDoi]
				,-SUM(tcdt.[SoLuongThucChayKM] + tcdt.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
				,-SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
				, N'Đối trừ: SP tối ưu [dbo].[ThucChay_PR_thucchaydatinh] do ' + dm.LyDo
				, dm.NgayThucHien
		FROM ABM_data_thucchay.dbo.[ThucChayDaTinh] tcdt
		INNER JOIN #DmThayDoi dm ON CAST(dm.ThucChayHopDongChiTietID AS NVARCHAR) = tcdt.DotChayBooking AND 
									dm.LoaiXuLy IN (1,2) 
        INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
		WHERE		tcdt.NgayThucHien < @NgayGhiNhan
			        AND hdct.HopDongChiTietID = dm.HopDongChitiet_BF
					AND tcdt.DmSanPhamREF IN (141,245,250,637,305)
					AND NOT(tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18)
		GROUP BY [HopDongID]
				,[SoHopDong]
				,[DmMaHopDongREF]
				,[TenMaHopDong]
				,[NgayDanhSoHopDong]
				,[NgayKyHopDong]
				,[NhanHopDong]
				,[NgayNhanBanFax]
				,[NgayNhanHopDongBanCung]
				,[NgayChuyenHopDongChoKeToan]
				,[So]
				,[Thang]
				,[Nam]
				,[GiaTriHopDong]
				,[CongNo]
				,[HopDongChiTietREF]
				,[DangSuDung]
				,[IsGiayPhep]
				,[TrangThaiHopDong]
				,[IsBanCung]
				,[DmPhongBanREF]
				,[TenPhongBan]
				,[DmBoPhanREF]
				,[TenBoPhan]
				,[DmNhomLamViecREF]
				,[TenNhomLamViec]
				,[DmDiaDiemLamViecREF]
				,[TenDiaDiemLamViec]
				,[SysNhanVienREF]
				,[TenDangNhap]
				,[TenNhanVien]
				,[TenKhachHang]
				,tcdt.[NhanHang]
				,tcdt.[DmNhomNganhREF]
				,tcdt.[TenNhomNganh]
				,[DmHinhThucQuangCao]
				,[TenHinhThucQuangCao]
				,tcdt.[DmSanPhamREF]
				,tcdt.[TenSanPham]
				,tcdt.[DmNhomWebsiteREF]
				,tcdt.[TenNhomWebsite]
				,tcdt.[DmChuyenMucREF]
				,tcdt.[TenChuyenMuc]
				,tcdt.[DmLoaiBannerREF]
				,tcdt.[TenLoaiBanner]
				,tcdt.[DmViTriREF]
				,tcdt.[TenViTri]
				,[SoLuongDotChayHD]
				,[DotChayBooking]
				,[SoLuongDotChayBooking]
				,tcdt.[SoLuong]
				,tcdt.[DonViTinh]
				,tcdt.[DonGia]
				,[DonGiaTheoDonVi]
				,tcdt.[ChietKhau]
				,tcdt.[GiamGia]
				,tcdt.[ThanhTien]
				,tcdt.[TiLeTuVan]
				,tcdt.[ChiPhiTuVan]
				,tcdt.[IsKhuyenMai]
				,tcdt.[KhuyenMai]
				,tcdt.[DmBannerREF]
				,tcdt.[DmChienDichREF]
				,tcdt.[DmWebsiteREF]
				,tcdt.[TenWebsite]
				,[TongViewThucChay]
				,[TongClickThucChay]
				,[TongSoBaiViet]
				,dm.LyDo
				,dm.NgayThucHien
		HAVING SUM(tcdt.[ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) <> 0
				OR SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) <> 0

		UPDATE  tchdct
        SET     tchdct.RecordStatus = 0
		FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct 
		JOIN @InsertedIDs I ON I.IDTreo = CAST(tchdct.ThucChayHopDongChiTietPRID AS NVARCHAR(100))

		DELETE
		FROM @InsertedIDs
		--=================================================== 3: Tính mới hoặc tính lại thực chạy ==============================
		INSERT INTO ABM_data_thucchay.dbo.ThucChayDaTinh
		(       ThucChayDaTinhID,
				HopDongID,
				SoHopDong,
				DmMaHopDongREF,
				TenMaHopDong,
				NgayDanhSoHopDong,
				NgayKyHopDong,
				NhanHopDong,
				NgayNhanBanFax,
				NgayNhanHopDongBanCung,
				NgayChuyenHopDongChoKeToan,
				So,
				Thang,
				Nam,
				GiaTriHopDong,
				CongNo,
				HopDongChiTietREF,
				DangSuDung,
				IsGiayPhep,
				TrangThaiHopDong,
				IsBanCung,
				DmPhongBanREF,
				TenPhongBan,
				DmBoPhanREF,
				TenBoPhan,
				DmNhomLamViecREF,
				TenNhomLamViec,
				DmDiaDiemLamViecREF,
				TenDiaDiemLamViec,
				SysNhanVienREF,
				TenDangNhap,
				TenNhanVien,
				TenKhachHang,
				NhanHang,
				DmNhomNganhREF,
				TenNhomNganh,
				DmHinhThucQuangCao,
				TenHinhThucQuangCao,
				DmSanPhamREF,
				TenSanPham,
				DmNhomWebsiteREF,
				TenNhomWebsite,
				DmChuyenMucREF,
				TenChuyenMuc,
				DmLoaiBannerREF,
				TenLoaiBanner,
				DmViTriREF,
				TenViTri,
				DotChayHopDong,
				SoLuongDotChayHD,
				DotChayBooking,
				SoLuongDotChayBooking,
				SoLuong,
				DonViTinh,
				DonGia,
				DonGiaTheoDonVi,
				ChietKhau,
				GiamGia,
				ThanhTien,
				TiLeTuVan,
				ChiPhiTuVan,
				IsKhuyenMai,
				KhuyenMai,
				DmBannerREF,
				DmChienDichREF,
				DmWebsiteREF,
				TenWebsite,
				TongViewThucChay,
				TongClickThucChay,
				TongSoBaiViet,
				SoLuongThucChay,
				NgayThucHien,
				GiaTriThayDoi,
				ThanhTienThucChayTruocTrietKhau,
				GiaTriTrietKhauThucChay,
				ThanhTienSauTrietKhauThucChay,
				GiaTriHoaHongThucChay,
				ThanhTienThucThu,
				ThanhTienKM,
				SoLuongThucChayKM,
				SoLuongThucChayLechTreoHa,
				ThanhTienLechTreoHa,
				CreatedAt,
				LastModifiedAt,
				IsPheDuyet,
				PheDuyetBy,
				PheDuyetAt,
				SoLuongThayDoi,
				SoLuongKMThayDoi,
				GiaTriKMThayDoi,
				GhiChu)
		OUTPUT INSERTED.DotChayBooking INTO @InsertedIDs
		SELECT  NEWID(),
				hd.HopDongID ,
				hd.SoHopDong ,
				hd.DmMaHopDongREF ,
				hd.TenMaHopDong,
				hd.NgayDanhSoHopDong ,
				hd.NgayKyHopDong ,
				ISNULL(hd.NhanHopDong, '') AS NhanHopDong ,
				hd.NgayNhanBanFax ,
				hd.NgayNhanHopDongBanCung ,
				hd.NgayChuyenHopDongChoKeToan ,
				hd.So ,
				hd.Thang ,
				hd.Nam , 
				hd.GiaTriHopDong ,
				hd.CongNo ,
				hdct.HopDongChiTietID ,
				hd.DangSuDung ,
				hd.IsGiayPhep ,
				hd.TrangThaiHopDong ,
				hd.IsBanCung , 
				hd.DmPhongBanREF ,
				ISNULL(hd.TenPhongBan, '') AS TenPhongBan ,
				hd.DmBoPhanREF ,
				ISNULL(hd.TenBoPhan, '') AS TenBoPhan ,
				hd.DmNhomLamViecREF ,
				ISNULL(hd.TenNhom, '') AS TenNhom ,
				hd.DmDiaDiemLamViecREF ,
				hd.TenDiaDiemLamViec ,
				hd.SysNhanVienREF ,
				ISNULL(hd.TenDangNhap, '') AS TenDangNhap ,
				hd.TenNhanVien , 
				hd.TenKhachHang , 
				dm.DmNhanHangREF ,
				hdct.DmNhomNganhREF ,
				hdct.TenNhomNganh , 
				hdct.DmLoaiREF AS DmHinhThucQuangCao ,
				hdct.TenLoai AS TenHinhThucQuangCao , 
				hdct.DmSanPhamREF AS DmSanPhamREF ,
				hdct.TenSanPham ,
				0 ,
				'' , 
				dm.DmChuyenMucREF,
				dm.TenChuyenMucREF ,
				hdct.DmLoaiBannerREF ,
				hdct.TenLoaiBanner ,
				hdct.DmViTriREF ,
				hdct.TenViTri ,
				'ThucChay_PR' DotChayHopDong ,
				0 AS SoLuongDotChayHD ,
				dm.ThucChayHopDongChiTietID DotChayBooking ,
				0 AS SoLuongDotChayBooking , 
				hdct.SoLuong AS SoLuong ,
				dbo.FormatDonViTinh(hdct.DonViTinh) AS DonViTinh ,
				hdct.DonGia AS DonGia , 
				dm.DonGiaTreo AS DonGiaTheoDonViTinh ,
				dm.ChietKhauTreo ChietKhau ,
				hdct.GiamGia ,
				hdct.ThanhTien ,
				hdct.TiLeTuVan ,
				hdct.ChiPhiTuVan ,
				hdct.IsKhuyenMai ,
				'' ,
				hdct.DmViTriREF AS DmBannerREF ,--haidh comment bo xung them dmvitriref = dmbannerref theo yeu cau ben ibiz 13062025
				0 DmChienDichREF ,
				dm.WebsiteREF,
				dm.TenWebsite,
				0 TongViewThucChay ,
				0 TongClickThucChay ,
				0 TongSoBaiViet ,
				SoLuongThucChay = IIF(dm.LoaiXuLy = 2, 0, IIF(hdct.IsKhuyenMai = 0, ISNULL(dm.SoLuong, 0), 0)),
				@NgayGhiNhan AS NgayThucHien ,
				IIF(dm.LoaiXuLy = 2, dm.ThanhTienSauCKTreo, 0) AS GiaTriThayDoi ,
				IIF(dm.LoaiXuLy = 2, 0, dm.SoLuong*dm.DonGiaTreo) AS ThanhTienThucChayTruocTrietKhau,
				IIF(dm.LoaiXuLy = 2, 0, dm.SoLuong*dm.DonGiaTreo*dm.ChietKhauTreo/100) AS GiaTriTrietKhauThucChay ,
				IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienSauCKTreo) AS ThanhTienSauTrietKhauThucChay ,
				IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienSauCKTreo * ISNULL(hdct.TiLeTuVan, 0)/100) AS GiaTriHoaHongThucChay ,
				IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienSauCKTreo *(1-ISNULL(hdct.TiLeTuVan, 0)/100)) AS ThanhTienThucThu ,
				IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienKhuyenMaiTreo) AS ThanhTienKM ,
				IIF(dm.LoaiXuLy = 2, 0, IIF( hdct.IsKhuyenMai = 1, dm.SoLuong, 0)) AS SoLuongThucChayKM ,
				0 SoLuongLechTreoHa ,
				0 ThanhTienLechTreoHa ,
				GETDATE() ,
				GETDATE() ,
				0 IsPheDuyet ,
				'' PheDuyetBy ,
				'' PheDuyetAt ,
				IIF(dm.LoaiXuLy = 2, IIF(hdct.IsKhuyenMai = 1, 0, dm.SoLuong), 0) SoLuongThayDoi ,
				IIF(dm.LoaiXuLy = 2, IIF( hdct.IsKhuyenMai = 1, dm.SoLuong, 0), 0) SoLuongKMThayDoi ,
				IIF(dm.LoaiXuLy = 2, dm.ThanhTienKhuyenMaiTreo, 0) GiaTriKMThayDoi ,
				IIF(dm.LoaiXuLy = 2, N'Tính lại: ', N'Tính mới: ') + N'SP tối ưu [dbo].[ThucChay_PR_ThucChayDaTinh] do ' + dm.LyDo
		FROM #DmThayDoi dm 
		INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON dm.HopDongChiTietID = hdct.HopDongChiTietID
		INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct ON tchdct.ThucChayHopDongChiTietPRID = dm.ThucChayHopDongChiTietID
		WHERE   dm.LoaiXuLy IN (2,3) AND 
			    hdct.DmSanPhamREF in (141,245,250,637,305) AND 
				NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) AND 
				ISNULL(tchdct.HopDongChiTietREF,0) <> 0
				AND tchdct.DmHinhThucQuangCaoREF <> 0
				AND tchdct.DmSanPhamREF <> 0
				AND tchdct.ThoiGianBatDau >= '2019-01-01'

		INSERT INTO thucchaydatinh_log
		SELECT  tcdt.*
		FROM dbo.ThucChayDaTinh tcdt
		JOIN @InsertedIDs I ON I.IDTreo = CAST(tcdt.DotChayBooking AS NVARCHAR(100))
		WHERE NgayThucHien = @NgayGhiNhan AND 
		      tcdt.DotChayHopDong = 'ThucChay_PR'

                             	
		UPDATE  tchdct
        SET     tchdct.RecordStatus = 1
		FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTietPR tchdct 
		JOIN @InsertedIDs I ON I.IDTreo = CAST(tchdct.ThucChayHopDongChiTietPRID AS NVARCHAR(100))

		DROP TABLE #DmThayDoi
	END


```
